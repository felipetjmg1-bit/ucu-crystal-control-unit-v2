
import hashlib
import datetime
import json

class ComponentTraceability:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
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

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def add_transaction(self, component_id, manufacturer, timestamp, location, status):
        transaction = {
            'component_id': component_id,
            'manufacturer': manufacturer,
            'timestamp': timestamp,
            'location': location,
            'status': status
        }
        self.pending_transactions.append(transaction)
        return self.get_last_block()['index'] + 1

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
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

# Exemplo de uso:
if __name__ == "__main__":
    blockchain = ComponentTraceability()

    print("Adicionando transações de componentes...")
    blockchain.add_transaction("COMP-001", "Fabricante A", str(datetime.datetime.now()), "Curvelo/MG", "Produzido")
    blockchain.add_transaction("COMP-002", "Fabricante B", str(datetime.datetime.now()), "São Paulo/SP", "Em Trânsito")

    last_block = blockchain.get_last_block()
    previous_proof = last_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)
    print(f"Novo bloco minerado: {block}")

    blockchain.add_transaction("COMP-003", "Fabricante A", str(datetime.datetime.now()), "Curvelo/MG", "Montado")

    last_block = blockchain.get_last_block()
    previous_proof = last_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_block(proof, previous_hash)
    print(f"Novo bloco minerado: {block}")

    print("\nCadeia de blocos:")
    for b in blockchain.chain:
        print(json.dumps(b, indent=4))

    print(f"A cadeia de blocos é válida? {blockchain.is_chain_valid(blockchain.chain)}")

    # Simulação de integração com DREX/Aurora Token
    print("\nSimulando integração com DREX/Aurora Token para rastreabilidade...")
    print("Tokens de rastreabilidade (representados por hashes de transação) seriam emitidos e associados a cada etapa do componente.")
    print("Esses tokens poderiam ser consultados na rede DREX/Aurora para verificar a autenticidade e o histórico do componente.")

