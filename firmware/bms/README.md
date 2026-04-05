# Firmware do Gerenciador de Bateria (BMS) para Células de Nióbio

Este diretório contém o firmware de baixo nível para o Gerenciador de Bateria (BMS) otimizado para baterias de estado sólido com ânodo de Nióbio, conforme especificado para a Unidade de Controle de Cristal (UCU) da fábrica de veículos elétricos em Curvelo/MG.

## Tecnologias Utilizadas

*   **C++**: Implementação de referência para sistemas embarcados de alta performance.
*   **Rust**: Implementação alternativa focada em segurança e concorrência.

## Funcionalidades Principais

*   **Leitura de Voltagem e Temperatura**: Monitoramento contínuo das células individuais da bateria.
*   **Verificação de Saúde da Célula**: Avaliação da condição operacional de cada célula com base em limites predefinidos.
*   **Balanceamento de Células (Simplificado)**: Lógica básica para balanceamento de carga entre as células.
*   **Otimização para Nióbio**: Preparado para integração com algoritmos específicos de carregamento e descarregamento para baterias de Nióbio.

## Estrutura do Diretório

*   `bms_firmware.cpp`: Código-fonte do firmware em C++.
*   `bms_firmware.rs`: Código-fonte do firmware em Rust.
*   `README.md`: Este arquivo de documentação.

## Como Compilar e Executar (Exemplo - C++)

Para compilar o código C++, você precisará de um compilador C++ (como `g++`).

```bash
g++ bms_firmware.cpp -o bms_firmware
./bms_firmware
```

## Como Compilar e Executar (Exemplo - Rust)

Para compilar o código Rust, você precisará do `cargo` (gerenciador de pacotes e sistema de build do Rust).

```bash
cargo new bms_firmware_rust --bin
cd bms_firmware_rust
# Copie o conteúdo de bms_firmware.rs para src/main.rs
# Adicione `rand = "0.8.5"` ao seu Cargo.toml na seção [dependencies]
cargo run
```

**Nota**: As implementações atuais são simulações para demonstrar a lógica. Em um ambiente real, elas seriam integradas a hardware específico e sistemas operacionais embarcados.
