# Link da apresentação: [TODO]
# Simulador de Gerenciamento de Memória Virtual (MMU)
Este repositório contém a implementação do Segundo Trabalho Prático da disciplina de Análise e Aplicação de Sistemas Operacionais da Universidade do Vale do Rio dos Sinos (UNISINOS).
O objetivo do projeto é simular o funcionamento de uma Unidade de Gerenciamento de Memória (MMU), traduzindo endereços virtuais para físicos, gerenciando Page Faults e aplicando políticas de substituição de páginas.
# Especificações do Sistema Simulado
O sistema foi modelado em Python seguindo os requisitos estabelecidos no enunciado, supondo um sistema com as seguintes características:
- Memória Principal (RAM): 64 KB (dividida em 8 frames)
- Memória Virtual: 1 MB (dividida em 128 páginas)
- Tamanho da Página e Frame: 8 KB (8192 bytes)
- Algoritmo de Substituição: LRU (Least Recently Used - Menos Recentemente Utilizada).
# Como Executar
Certifique-se de ter o Python 3.x instalado em sua máquina. Para rodar o simulador, execute o seguinte comando no terminal:
```bash
python simulador.py
```
## Fluxo de Execução

```mermaid
graph TD
    %% Nós e Conexões Principais
    A([Processo / Thread]) -->|Solicita Endereço Virtual| B(MMU)
    B --> C{Consulta Tabela<br>de Páginas}
    
    %% Ramificação de Hit
    C -->|Página Presente| D[Page Hit]
    D --> E[Calcula Endereço Físico:<br>Frame * 8192 + Offset]
    
    %% Ramificação de Fault
    C -->|Página Ausente| F[Page Fault<br>Falta de Página]
    F --> G{Existem Frames<br>Livres?}
    
    G -->|Sim| H[Aloca no primeiro<br>Frame livre disponível]
    G -->|Não| I[Algoritmo LRU:<br>Remove a página mais antiga da lista]
    I --> J[Invalida a Página antiga<br>na Tabela]
    J --> K[Carrega a Nova Página<br>no Frame liberado]
    
    H --> L[Atualiza Tabela de Páginas e<br>Memória Física]
    K --> L
    L --> E
    
    %% Fim
    E --> M[Atualiza Fila LRU<br>Move página para o fim]
    M --> N([Apresenta Endereço Físico<br>e Conteúdo])

    %% Estilos (Classes)
    classDef startStop fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef process fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef decision fill:#fff9c4,stroke:#fbc02d,stroke-width:2px;
    classDef mmu fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;
    classDef fault fill:#ffebee,stroke:#f44336,stroke-width:2px;

    %% Atribuição das Classes aos Nós
    class A,N startStop;
    class D,E,H,J,K,L,M process;
    class C,G decision;
    class B mmu;
    class F,I fault;
```

