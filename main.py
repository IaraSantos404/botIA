from arena import gerar_arena
import random

QUANT_PAREDES = 25
QUANT_ARMADILHAS = 6
QUANT_MINERIOS = 12
LARGURA = 15
ALTURA = 9

SEED = random.randint(0, 1000)

if __name__ == "__main__":
    gerar_arena(LARGURA, ALTURA, QUANT_PAREDES, QUANT_MINERIOS, QUANT_ARMADILHAS, SEED)