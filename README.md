# Link da apresentação: https://youtu.be/e_oijN3F_UY
# Simulador de Gerenciamento de Memória Virtual (MMU)
Este repositório contém a implementação do Segundo Trabalho Prático da disciplina de Sistemas Operacionais: Análise e Aplicações da Universidade do Vale do Rio dos Sinos (UNISINOS).
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
    A([Processo / Thread]) -->|Solicita Endereço Virtual| B(MMU)
    B --> C{Consulta Tabela<br>de Páginas}
    
    C -->|Página Presente| D[Page Hit]
    D --> E[Calcula Endereço Físico:<br>Frame * 8192 + Offset]
    
    C -->|Página Ausente| F[Page Fault<br>Falta de Página]
    F --> G{Existem Frames<br>Livres?}
    
    G -->|Sim| H[Aloca no primeiro<br>Frame livre disponível]
    G -->|Não| I[Algoritmo LRU:<br>Remove a página mais antiga da lista]
    I --> J[Invalida a Página antiga<br>na Tabela]
    J --> K[Carrega a Nova Página<br>no Frame liberado]
    
    H --> L[Atualiza Tabela de Páginas e<br>Memória Física]
    K --> L
    L --> E
    
    E --> M[Atualiza Fila LRU<br>Move página para o fim]
    M --> N([Apresenta Endereço Físico<br>e Conteúdo])
```


# Python-MMU-Simulator
Simulador de MMU em Python para a disciplina de Sistemas Operacionais: Análise e Aplicações
