# T2 - Filas de Prioridade (heap binario de maximo em C99)

Trabalho de pesquisa e implementacao sobre filas de prioridade implementadas como heaps binarios: relatorio em
PDF (conceitos, propriedades, armazenamento em vetor, passo a passo do upheap e do downheap, pseudocodigos e
complexidade) e um programa em C com menu para inserir, remover e imprimir o heap.

**Grupo:** Diego Kelme Santos da Silva, Gabriel Sangoi e Pedro Klein · **Entrega:** 26/11/2026, por e-mail

## Estrutura do Projeto

- `heap.c`: o programa (heap de maximo guardado em vetor, `MAX` = 150).
- `relatorio/relatorio.tex`: fonte do relatorio, em ABNT no modelo do MDT da UFSM (classe `abntex2`).
- `relatorio/figuras.py`: gera as figuras do relatorio em `relatorio/figuras/`.
- `entrega/`: exatamente o que vai anexado no e-mail (`heap.c` e o PDF do relatorio). Sem `.exe`.

## Compilacao e Execucao

```bash
gcc -Wall -Wextra -std=c99 -o heap heap.c
./heap                # no Windows: heap.exe
```

Menu:

```
1 - Inserir                    (le varios valores, ate digitar s)
2 - Remover (maior)            (remove a raiz e mostra o valor removido)
3 - Imprimir                   (No <valor>: filho esq: <valor|vazio>, filho dir: <valor|vazio>)
4 - Remover valor especifico   (busca o valor, troca com o ultimo e reajusta)
0 - Sair
```

Com o exemplo do enunciado (inserir 1, 2 e 3, imprimir, remover, imprimir) a saida e':

```
No 3: filho esq: 1, filho dir: 2
No 1: filho esq: vazio, filho dir: vazio
No 2: filho esq: vazio, filho dir: vazio
Removido: 3
No 2: filho esq: 1, filho dir: vazio
No 1: filho esq: vazio, filho dir: vazio
```

## Relatorio

```bash
cd relatorio
uv run --with matplotlib python figuras.py    # so se mudar alguma figura
pdflatex relatorio.tex && pdflatex relatorio.tex
```

A segunda passada do `pdflatex` acerta o sumario e as referencias a figuras e quadros.

## Decisoes

- A opcao 2 remove a raiz, como numa fila de prioridade e como no exemplo do enunciado. A remocao de um valor
  qualquer ficou como opcao 4, com custo O(n) por causa da busca.
- A impressao segue o formato do enunciado, em ordem de posicao no vetor. Sem acento no "No" para nao quebrar
  no terminal do Windows.
- Entrada que nao e' numero (ou linha vazia) e' recusada com "Valor invalido!" em vez de virar 0, e fim de
  entrada (EOF) encerra o programa em vez de travar no menu.
- As figuras sao proprias, com indices a partir de 0, iguais as formulas usadas no codigo:
  pai `(i - 1) / 2`, filhos `2i + 1` e `2i + 2`.
