import math, os, textwrap
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['savefig.bbox'] = 'tight'
matplotlib.rcParams['savefig.pad_inches'] = 0.1
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle, Patch
from matplotlib.lines import Line2D

# gera as figuras do relatorio em relatorio/figuras/
# uso: uv run --with matplotlib python figuras.py
SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figuras')
os.makedirs(SAIDA, exist_ok=True)

AZUL, BORDA = '#dbe9f6', '#2b4c6f'
LARANJA, AMARELO, VERMELHO, VERDE = '#f6b26b', '#fff2a8', '#f4a3a3', '#c9e7c1'
TROCA = '#c0392b'
W, DY, R, NIVEIS, CW = 8.0, 1.25, 0.36, 3, 0.9


def pos(i):
    nivel = int(math.floor(math.log2(i + 1)))
    k = i - (2 ** nivel - 1)
    return (k + 0.5) * W / 2 ** nivel, -nivel * DY


def celula(i):
    n = 2 ** NIVEIS - 1
    x0 = (W - n * CW) / 2
    yv = -(NIVEIS - 1) * DY - 1.35
    return x0 + i * CW, yv


def desenha(ax, arr, cores=None, trocas=(), movimentos=(), titulo=None, texto=None, vetor=True):
    cores = cores or {}
    for i in range(1, len(arr)):
        (x1, y1), (x2, y2) = pos((i - 1) // 2), pos(i)
        ax.plot([x1, x2], [y1, y2], color=BORDA, lw=1.4, zorder=1)
    for i, v in enumerate(arr):
        x, y = pos(i)
        ax.add_patch(Circle((x, y), R, facecolor=cores.get(i, AZUL), edgecolor=BORDA, lw=1.6, zorder=2))
        ax.text(x, y, str(v), ha='center', va='center', fontsize=13, fontweight='bold', zorder=3)
        ax.text(x, y - R - 0.08, f'[{i}]', fontsize=8.5, color='#555', ha='center', va='top', zorder=3)
    for a, b in trocas:
        ax.add_patch(FancyArrowPatch(pos(a), pos(b), arrowstyle='<->', connectionstyle='arc3,rad=0.45',
                                     color=TROCA, lw=2, mutation_scale=16, shrinkA=16, shrinkB=16, zorder=4))
    for a, b in movimentos:
        ax.add_patch(FancyArrowPatch(pos(a), pos(b), arrowstyle='->', connectionstyle='arc3,rad=-0.35',
                                     color=TROCA, lw=1.8, ls='--', mutation_scale=16, shrinkA=16, shrinkB=16, zorder=4))
    ymin = -(NIVEIS - 1) * DY - 0.6
    if vetor:
        n = 2 ** NIVEIS - 1
        for i in range(n):
            x, yv = celula(i)
            fc = cores.get(i, 'white') if i < len(arr) else '#eeeeee'
            ax.add_patch(Rectangle((x, yv), CW, 0.6, facecolor=fc, edgecolor=BORDA, lw=1.2))
            if i < len(arr):
                ax.text(x + CW / 2, yv + 0.3, str(arr[i]), ha='center', va='center', fontsize=11)
            ax.text(x + CW / 2, yv - 0.22, str(i), ha='center', va='center', fontsize=8.5, color='#555')
        x0, yv = celula(0)
        ax.text(x0 - 0.15, yv + 0.3, 'vetor', ha='right', va='center', fontsize=9, color='#555')
        ax.text(celula(n - 1)[0] + CW + 0.15, yv + 0.3, f'tam = {len(arr)}', ha='left', va='center', fontsize=9, color='#555')
        ymin = yv - 0.55
    if titulo:
        ax.set_title(titulo, loc='left', fontsize=12, fontweight='bold')
    if texto:
        ax.text(0.0, -0.02, textwrap.fill(texto, 62), transform=ax.transAxes, ha='left', va='top', fontsize=10)
    ax.set_xlim(-1.0, W + 1.0)
    ax.set_ylim(ymin, 0.6)
    ax.set_aspect('equal')
    ax.axis('off')


def legenda(fig, itens):
    hs = []
    for tipo, cor, rotulo in itens:
        if tipo == 'patch':
            hs.append(Patch(facecolor=cor, edgecolor=BORDA, label=rotulo))
        else:
            hs.append(Line2D([0], [0], color=TROCA, lw=2, ls=tipo, label=rotulo))
    fig.legend(handles=hs, loc='lower center', ncol=len(hs), frameon=False, fontsize=10)


def passo_a_passo(nome, passos, itens_legenda):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8.6))
    for ax, p in zip(axs.flat, passos):
        desenha(ax, **p)
    legenda(fig, itens_legenda)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.96, bottom=0.12, hspace=0.42, wspace=0.08)
    fig.savefig(os.path.join(SAIDA, nome), dpi=150)
    plt.close(fig)


# 1) insercao do 45 com upheap
passo_a_passo('fig_insercao_upheap.png', [
    dict(arr=[40, 38, 30, 20, 10], titulo='Passo 1',
         texto='Heap de máximo inicial com 5 elementos. Vamos inserir o valor 45.'),
    dict(arr=[40, 38, 30, 20, 10, 45], cores={5: LARANJA, 2: AMARELO}, trocas=[(5, 2)], titulo='Passo 2',
         texto='O 45 entra na primeira posição livre do vetor (índice 5). Upheap: o pai do índice 5 é '
               '(5 - 1) / 2 = 2, que guarda 30. Como 45 > 30, os dois trocam de lugar.'),
    dict(arr=[40, 38, 45, 20, 10, 30], cores={2: LARANJA, 0: AMARELO}, trocas=[(2, 0)], titulo='Passo 3',
         texto='Agora o 45 está no índice 2. O pai é (2 - 1) / 2 = 0, que guarda 40. Como 45 > 40, trocam de novo.'),
    dict(arr=[45, 38, 40, 20, 10, 30], cores={0: LARANJA}, titulo='Passo 4',
         texto='O 45 chegou à raiz (índice 0) e o upheap termina. Todo pai é maior ou igual aos filhos: '
               'o heap é válido.'),
], [('patch', LARANJA, 'elemento sendo ajustado'), ('patch', AMARELO, 'pai comparado'), ('-', None, 'troca')])

# 2) remocao do maior (raiz) com downheap
passo_a_passo('fig_remocao_downheap.png', [
    dict(arr=[45, 38, 40, 20, 10, 30], cores={0: VERMELHO}, titulo='Passo 1',
         texto='Em uma fila de prioridade, a remoção retira a raiz, que guarda o maior valor (45).'),
    dict(arr=[45, 38, 40, 20, 10, 30], cores={0: VERMELHO, 5: LARANJA}, movimentos=[(5, 0)], titulo='Passo 2',
         texto='O último elemento do vetor (30, índice 5) é copiado para a raiz e o tamanho do heap '
               'diminui de 6 para 5. O 45 sai da estrutura.'),
    dict(arr=[30, 38, 40, 20, 10], cores={0: LARANJA, 1: AMARELO, 2: AMARELO}, trocas=[(0, 2)], titulo='Passo 3',
         texto='Downheap: o 30 é comparado com os filhos, 38 (índice 1) e 40 (índice 2). O maior filho é o 40 '
               'e, como 30 < 40, os dois trocam de lugar.'),
    dict(arr=[40, 38, 30, 20, 10], cores={2: LARANJA}, titulo='Passo 4',
         texto='O 30 está agora no índice 2. Os filhos seriam os índices 5 e 6, que não existem (tam = 5), '
               'então o downheap termina. O heap é válido e a raiz guarda o novo maior valor, 40.'),
], [('patch', VERMELHO, 'elemento removido'), ('patch', LARANJA, 'elemento sendo ajustado'),
    ('patch', AMARELO, 'filhos comparados'), ('-', None, 'troca'), ('--', None, 'cópia do último para a raiz')])

# 3) heap de maximo e heap de minimo (so a arvore)
for nome, arr in [('fig_heap_maximo.png', [30, 25, 19, 16, 9, 7, 5]),
                  ('fig_heap_minimo.png', [5, 9, 7, 16, 25, 19, 30])]:
    fig, ax = plt.subplots(figsize=(7, 3.6))
    desenha(ax, arr, vetor=False)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(os.path.join(SAIDA, nome), dpi=150, bbox_inches='tight')
    plt.close(fig)

# 4) armazenamento em vetor (indices a partir de 0)
fig, ax = plt.subplots(figsize=(7.5, 6))
arr = [30, 25, 19, 16, 9, 7, 5]
desenha(ax, arr, cores={1: AMARELO, 3: VERDE, 4: VERDE, 0: LARANJA})
_, yv = celula(0)
topo = yv + 0.6
def centro(i):
    return celula(i)[0] + CW / 2
for alvo, rot, rad in [(3, '2·1 + 1 = 3', -0.55), (4, '2·1 + 2 = 4', -0.6)]:
    ax.add_patch(FancyArrowPatch((centro(1), topo), (centro(alvo), topo), arrowstyle='->',
                                 connectionstyle=f'arc3,rad={rad}', color='#2e7d32', lw=1.6, mutation_scale=14))
ax.add_patch(FancyArrowPatch((centro(1), yv), (centro(0), yv), arrowstyle='->', connectionstyle='arc3,rad=-0.8',
                             color='#b45f06', lw=1.6, mutation_scale=14))
ax.text(W / 2, yv - 0.85, 'Para o índice i = 1 (valor 25): filho esquerdo em 2i + 1 = 3, filho direito em 2i + 2 = 4, '
        '\npai em (i - 1) / 2 = 0 (divisão inteira).', ha='center', va='top', fontsize=9.5)
ax.set_ylim(yv - 1.7, 0.6)
fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
fig.savefig(os.path.join(SAIDA, 'fig_vetor_indices.png'), dpi=150)
plt.close(fig)

print('\n'.join(sorted(os.listdir(SAIDA))))
