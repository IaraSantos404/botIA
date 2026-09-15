from arena import desenhar_arena, gerar_arena
import random
from agente import Agente
from logica import BaseConhecimento
from geral import *
import time

QUANT_PAREDES = 25
QUANT_ARMADILHAS = 6
QUANT_MINERIOS = 12
LARGURA = 15
ALTURA = 9

SEED = random.randint(0, 1000)

def new_game():
    paredes, armadilhas, minerios = gerar_arena(LARGURA, ALTURA, QUANT_PAREDES, QUANT_MINERIOS, QUANT_ARMADILHAS, SEED)
    agente_alfa = Agente((0, 0), "Alfa")
    agente_beta = Agente((LARGURA - 1, ALTURA - 1), "Beta")
    agentes = [agente_alfa, agente_beta]
    
    return paredes, armadilhas, minerios, agentes

def game_over(agentes, minerios):
    alfa = agentes[0]
    beta = agentes[1]

    alvos_restantes = {
        pos for pos in minerios if pos not in alfa.alvos_descartados
        and pos not in beta.alvos_descartados
    }

    if alfa.bateria <= 0 and beta.bateria <= 0:
        return True
    elif not alvos_restantes and alfa.carga == 0 and beta.carga == 0:
        return True

    return False

def update_route(agente, rival, minerios, paredes, armadilhas):
    if agente.alvo is None or (agente.alvo not in minerios and agente.alvo != agente.pos_base) :
        melhor_alvo = minimax(agente, rival.posicao, minerios)
        agente.alvo = melhor_alvo

   
    if agente.alvo is not None:
        caminho = a_estrela(LARGURA, ALTURA, paredes, armadilhas, agente.posicao, agente.alvo)
        if caminho:
            agente.caminho = caminho
        elif agente.posicao != agente.alvo:
            if agente.alvo != agente.pos_base:
                agente.alvos_descartados.add(agente.alvo)
                agente.alvo = None


def agent_action(agente, armadilhas, minerios):
    if agente.caminho:
        proximo_passo = agente.caminho.pop(0)
        if proximo_passo in armadilhas:
            agente.bateria -= 4
        else:
            agente.bateria -= 2

        agente.posicao = proximo_passo

        if agente.posicao in minerios:
            agente.tentar_coletar(minerios)

        if agente.posicao == agente.pos_base:
            agente.recarregar()


def print_game_state(agente_atual, turno):
    print(f"Turno: {turno}")
    print(f"Agente Atual: {agente_atual.nome} posição: {agente_atual.posicao}, Bateria: {agente_atual.bateria}, Carga: {agente_atual.carga}, Pontuação: {agente_atual.pontuacao}")
    


def main():
    turnos = 0
    paredes, armadilhas, minerios, agentes = new_game()

    while not game_over(agentes, minerios):
        agente_atual = agentes[turnos % 2]
        agente_rival = agentes[(turnos + 1) % 2]

        if agente_atual.bateria <=0:
            turnos += 1
            continue

        update_route(agente_atual, agente_rival, minerios, paredes, armadilhas)
        agent_action(agente_atual, armadilhas, minerios)
        desenhar_arena(LARGURA, ALTURA, paredes, armadilhas, minerios, agentes)
        print_game_state(agente_atual, turnos)
        time.sleep(1)

        turnos+=1

    if game_over(agentes, minerios):
        print("Jogo encerrado!")
        for i, agente in enumerate(agentes):
            print(f"Agente: {agente.nome} - Pontuação = {agente.pontuacao}, Bateria = {agente.bateria}, Carga = {agente.carga}")

        if agentes[0].pontuacao > agentes[1].pontuacao:
            print(f"Agente {agentes[0].nome} venceu!")
        elif agentes[0].pontuacao < agentes[1].pontuacao:
            print(f"Agente {agentes[1].nome} venceu!")

    
if __name__ == "__main__":
    main()
