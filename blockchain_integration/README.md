# Módulo de Integração Blockchain DREX/Aurora para Rastreabilidade de Componentes

Este módulo demonstra a integração de um protocolo de rastreabilidade de componentes utilizando uma simulação de blockchain, com foco na compatibilidade com as redes DREX e Aurora Token.

## Contexto

Para a fábrica de veículos elétricos em Curvelo/MG, a rastreabilidade de componentes é crucial para garantir a qualidade, autenticidade e conformidade regulatória. A integração com tecnologias blockchain, como DREX e Aurora Token, oferece uma solução robusta para este desafio.

## Funcionalidades

*   **Registro Imutável**: Cada etapa do ciclo de vida de um componente (produção, transporte, montagem, etc.) é registrada como uma transação em uma cadeia de blocos.
*   **Verificação de Autenticidade**: A natureza descentralizada e imutável da blockchain permite verificar a autenticidade e a origem de cada componente.
*   **Transparência**: O histórico completo de um componente pode ser auditado por partes autorizadas na rede.
*   **Integração com DREX/Aurora**: Simula a emissão de tokens de rastreabilidade (representados por hashes de transação) que seriam associados a cada etapa do componente e consultáveis nas redes DREX/Aurora.

## Estrutura do Diretório

*   `drex_aurora_integration.py`: Script Python que simula a lógica de uma blockchain para rastreabilidade de componentes.
*   `README.md`: Este arquivo de documentação.

## Como Funciona (Simulação)

O script `drex_aurora_integration.py` implementa uma blockchain simplificada onde:

1.  **Transações de Componentes**: São adicionadas informações sobre o `component_id`, `manufacturer`, `timestamp`, `location` e `status`.
2.  **Mineração de Blocos**: As transações pendentes são agrupadas em blocos, que são então "minerados" usando um algoritmo de Prova de Trabalho (Proof of Work) simplificado.
3.  **Cadeia Imutável**: Cada bloco é encadeado ao anterior através de um hash criptográfico, garantindo a integridade da cadeia.

## Integração com DREX/Aurora Token

Em um cenário real, os hashes das transações ou identificadores únicos dos componentes seriam tokenizados nas redes DREX/Aurora. Isso permitiria:

*   **Tokens de Rastreabilidade**: Cada componente ou lote de componentes teria um token digital correspondente na blockchain.
*   **Consulta Pública/Privada**: Partes interessadas poderiam consultar o histórico do token na rede DREX/Aurora para verificar a procedência e o status do componente.
*   **Contratos Inteligentes**: Poderiam ser implementados contratos inteligentes para automatizar verificações de conformidade ou acionar ações com base no status do componente na blockchain.

## Como Executar a Simulação

Para executar o script Python, certifique-se de ter Python 3 instalado e a biblioteca `rand` (se não estiver usando `random` padrão).

```bash
python3 drex_aurora_integration.py
```

Este script irá imprimir a cadeia de blocos simulada e demonstrar como as transações de componentes seriam registradas e verificadas.
