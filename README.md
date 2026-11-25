# Estrutura de Dados

> Trabalhos, exercícios e material da disciplina de Estrutura de Dados da UFSM, em C.

**Contexto:** UFSM · Sistemas de Informação · Estrutura de Dados · Profª Deise de Brum Saccol · 2026/2

## Sobre

Repositório da disciplina para o semestre 2026/2. Ainda não há código: os trabalhos, exercícios e materiais entram aqui ao longo do semestre, nas pastas descritas abaixo.

| | |
|---|---|
| **Aulas** | Terças e quintas, 10h30 |
| **Local** | Lab 361, 3º andar do anexo A do Centro de Tecnologia (CT) |
| **Linguagem** | C |
| **Provas de anos anteriores** | [ufsm-si-provas-passadas](https://github.com/itskelme/ufsm-si-provas-passadas) |

## Conteúdo

### Tópicos previstos

A lista abaixo não é a ementa oficial: são os assuntos que costumam compor Estrutura de Dados em C, usados aqui para organizar o estudo. Ela será ajustada conforme o plano de ensino da professora.

| Tópico | O que envolve |
|---|---|
| Revisão de C | Ponteiros, aritmética de ponteiros, `struct`, passagem por referência |
| Alocação dinâmica | `malloc`, `calloc`, `realloc`, `free`; vetores e matrizes dinâmicos |
| Tipos abstratos de dados (TAD) | Separação entre interface (`.h`) e implementação (`.c`) |
| Listas | Lista sequencial (vetor); listas encadeadas simples, duplamente encadeadas e circulares |
| Pilhas | Implementação com vetor e com lista; aplicações (expressões, balanceamento de parênteses) |
| Filas | Fila com vetor circular e com lista; fila de prioridade |
| Recursão | Funções recursivas e uso em estruturas (listas e árvores) |
| Árvores | Árvores binárias, percursos (pré, em e pós-ordem), árvores binárias de busca; balanceamento (AVL) |
| Heap | Heap binário e heapsort |
| Tabelas hash | Funções de espalhamento, tratamento de colisões |
| Ordenação e busca | Bubble, insertion, selection, merge e quick sort; busca sequencial e binária |
| Complexidade | Noções de análise de algoritmos e notação O |

### Trabalhos e exercícios

| Pasta | Conteúdo | Situação |
|---|---|---|
| `trabalhos/` | Trabalhos avaliativos, um por subpasta (`t1-...`, `t2-...`) | A publicar |
| `exercicios/` | Exercícios de aula e listas | A publicar |
| `material/` | Slides, enunciados e material de apoio da disciplina | A publicar |

## Tecnologias / Formatos

- **C** (padrão C99), compilado com **GCC**
- **Make** (opcional), para trabalhos com mais de um arquivo
- **Valgrind** (Linux) ou **AddressSanitizer** (`-fsanitize=address`) para encontrar vazamentos de memória
- **PDF** para material e enunciados

## Estrutura do projeto

Estrutura planejada:

```
ufsm-si-estrutura-de-dados/
├── trabalhos/
│   └── t1-<tema>/         # código, enunciado e README de cada trabalho
├── exercicios/
│   └── <assunto>/         # exercícios de aula agrupados por tema
├── material/              # slides e material da disciplina
├── LICENSE
└── README.md
```

## Como rodar

Cada trabalho vai ter instruções próprias no seu README. O padrão geral de compilação:

```bash
# programa de um arquivo
gcc -Wall -Wextra -std=c99 -o programa programa.c

# programa dividido em TAD (lista.h, lista.c, main.c)
gcc -Wall -Wextra -std=c99 -o programa main.c lista.c
./programa
```

Para checar vazamentos de memória, importante em estruturas alocadas dinamicamente:

```bash
# Linux
valgrind --leak-check=full ./programa

# GCC/Clang com AddressSanitizer
gcc -Wall -std=c99 -g -fsanitize=address -o programa main.c lista.c
```

No Windows, o GCC pode ser instalado pelo [MSYS2](https://www.msys2.org/) ou usado via WSL.

## Referências

Referências gerais da área (a bibliografia oficial será a do plano de ensino):

- CELES, W.; CERQUEIRA, R.; RANGEL, J. L. *Introdução a Estruturas de Dados: com técnicas de programação em C*. 2. ed. Rio de Janeiro: Elsevier, 2016.
- TENENBAUM, A. M.; LANGSAM, Y.; AUGENSTEIN, M. J. *Estruturas de Dados Usando C*. São Paulo: Makron Books, 1995.
- ZIVIANI, N. *Projeto de Algoritmos com Implementações em Pascal e C*. 3. ed. São Paulo: Cengage Learning, 2010.
- CORMEN, T. H. et al. *Algoritmos: Teoria e Prática*. 3. ed. Rio de Janeiro: Elsevier, 2012.
- FEOFILOFF, P. *Projeto de Algoritmos em C*: <https://www.ime.usp.br/~pf/algoritmos/>
- Referência da biblioteca padrão de C: <https://en.cppreference.com/w/c>

## Autores

- Diego Kelme Santos da Silva — [@itskelme](https://github.com/itskelme)
- Profª Deise de Brum Saccol (UFSM) — material e enunciados da disciplina, quando publicados aqui

## Licença

Este projeto está sob a licença [CC BY-NC 4.0](LICENSE): uso pessoal e modificação permitidos com atribuição; uso comercial proibido. Material de terceiros (slides, provas, enunciados) pertence aos respectivos autores e não é coberto por esta licença.
