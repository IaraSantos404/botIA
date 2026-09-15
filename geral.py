import heapq
import arena
# resumo geral so que precisa ser feito

def validacao(x, y, paredes, largura, altura):
    return 0 <= x < largura and 0 <= y < altura and (x,y) not in paredes 

# Busca
def vizinhos(largura, altura, posicoes_parede, pos_atual):
    x, y = pos_atual
    movimentos = [(1,0),(0,1), (-1,0),(0,-1)]
    vizinhos = [(x+dx, y+dy) for dx, dy in movimentos]
    return [v for v in vizinhos if validacao(*v,posicoes_parede, largura, altura)]
# Responsável por:
# heurística;
def h_manhattan(x,y):
    return abs(x[0] - y[0]) + abs(x[1]+y[1])

# A*
def a_estrela(largura, altura, posicoes_paredes, posicoes_armadilhas,inicio, alvo):
    front = []
    heapq.heappush(front,(0,inicio))
    custo_acumulado = {inicio:0}
    pai = {inicio: None}

    while front:
        _,atual = heapq.heappop(front)
        if atual == alvo:
            break
        for prox in vizinhos(largura, altura, posicoes_paredes, atual):
            custo_passo = 2 if prox in posicoes_armadilhas else 1
            novo_custo = custo_acumulado[atual] + custo_passo

            if prox not in custo_acumulado or novo_custo < custo_acumulado[prox]:
                custo_acumulado[prox] = novo_custo
                prioridade = novo_custo + h_manhattan(prox , alvo)
                heapq.heappush(front,(prioridade, prox))
                pai[prox] = atual


    caminho = []
    atual = alvo 
    if atual not in pai:
        return []

    while atual != inicio:
        caminho.append(atual)
        atual = pai[atual]

    caminho.reverse()
    return caminho
# comparação com outro algoritmo.


# Estratégia  
# Responsável por:
# função de avaliação
def avaliar_vantagem(pos_robo , pos_inimigo, alvo):
    dist_robo = h_manhattan(pos_robo,alvo['pos'])
    dist_inimigo = h_manhattan(pos_inimigo,alvo['pos'])
    vantagem = dist_inimigo - dist_robo
    return alvo['valor'] + vantagem
# Minimax;

def minimax():
    # para implementar preciso saber como as informações dos robores vao ser armazenados p acessar

# alfa-beta;

# Lógica
# Responsável por:

# fatos;
# regras;
# encadeamento para frente.

# Simulação
# Responsável por:

# turnos;
# ordem das decisões;
# encerramento da partida.