import hashlib
import datetime
import json
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Transaction(BaseModel):
    component_id: str
    manufacturer: str
    location: str
    status: str
    timestamp: Optional[str] = None

class ComponentTraceability:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof: int, previous_hash: str) -> dict:
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def get_last_block(self) -> dict:
        return self.chain[-1]

    def hash(self, block: dict) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_transaction(self, component_id: str, manufacturer: str, location: str, status: str) -> int:
        transaction = {
            'component_id': component_id,
            'manufacturer': manufacturer,
            'timestamp': str(datetime.datetime.now()),
            'location': location,
            'status': status
        }
        self.pending_transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def proof_of_work(self, previous_proof: int) -> int:
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def is_chain_valid(self) -> bool:
        previous_block = self.chain[0]
        block_index = 1
        while block_index < len(self.chain):
            block = self.chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# API Implementation
app = FastAPI(title="DREX Aurora Traceability Connector")
blockchain = ComponentTraceability()

@app.get("/chain")
def get_chain():
    return {
        "length": len(blockchain.chain),
        "chain": blockchain.chain,
        "is_valid": blockchain.is_chain_valid()
    }

@app.post("/transaction/new")
def add_transaction(tx: Transaction):
    index = blockchain.add_transaction(
        tx.component_id, tx.manufacturer, tx.location, tx.status
    )
    return {"message": f"Transação será adicionada ao Bloco {index}"}

@app.get("/mine")
def mine():
    last_block = blockchain.get_last_block()
    previous_proof = last_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)
    
    return {
        "message": "Novo bloco minerado com sucesso!",
        "index": block['index'],
        "transactions": block['transactions'],
        "proof": block['proof'],
        "previous_hash": block['previous_hash']
    }

@app.get("/drex/verify/{component_id}")
def verify_drex(component_id: str):
    # Simulação de verificação na rede DREX/Aurora
    history = []
    for block in blockchain.chain:
        for tx in block['transactions']:
            if tx['component_id'] == component_id:
                history.append(tx)
    
    if not history:
        raise HTTPException(status_code=404, detail="Componente não encontrado na rede Aurora")
        
    return {
        "component_id": component_id,
        "verified_by": "Aurora DREX Node",
        "history": history,
        "status": "AUTHENTIC"
    }

if __name__ == "__main__":
    import uvicorn
    print("Iniciando Conector de Rastreabilidade DREX Aurora...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
