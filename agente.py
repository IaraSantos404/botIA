# Responsável por: Controlar o robô
from logica import configurar_bc_robo

class Agente:
    def __init__(self, pos_inicial):

        self.posição = pos_inicial
        self.bateria = 100
        self.carga = 0
        self.maxCarga = 3
        self.pontuacao = 0
        self.baseDeConhecimento = configurar_bc_robo()
        self.caminho = []
        self.alvo = None
        self.alvos_descartados = set()
    def lerSensores(self):
        return {
            'bateria_alta': self.bateria > 20,
            'carga_cheia': self.carga >= self.maxCarga,
        }
    def tentar_coletar(self, mapa):
        sensores = self.lerSensores()
        interferencias = self.baseDeConhecimento.interferir(sensores)

        if 'coleta_permitida' in interferencias and self.pos in mapa.minerios:
            minerio = mapa.minerios[self.pos]
            self.carga += 1
            self.pontuacao += minerio['valor']
            mapa.remover_minerio(*self.pos)
            self.alvo = None
            return True
        return False
    def recarregar(self):
        if self.carga > 0:
            self.pontuacao += self.carga * 10
            self.carga = 0
            self.baseDeConhecimento
            self.alvos_descartados.clear()
            self.alvo = None

# Preciso de uma forma de saber o quanto custa meu caminho, para determinar quando voltar
