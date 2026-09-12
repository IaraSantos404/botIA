from arena import gerar_arena
import random
import geral

QUANT_PAREDES = 25
QUANT_ARMADILHAS = 6
QUANT_MINERIOS = 12
LARGURA = 15
ALTURA = 9

SEED = random.randint(0, 1000)

if __name__ == "__main__":
    posicoes_paredes, posicoes_armadilhas, minerios = gerar_arena(LARGURA, ALTURA, QUANT_PAREDES, QUANT_MINERIOS, QUANT_ARMADILHAS, SEED)
    caminho = geral.a_estrela(LARGURA, ALTURA, posicoes_paredes, posicoes_armadilhas,(0,0),(7,6))
    print(caminho)