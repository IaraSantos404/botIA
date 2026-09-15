class BaseConhecimento:
    def __init__(self):
        self.regras = []
    def adicionar_regra(self, condicao, acao):
        self.regras.append((condicao, acao))
    def interferir(self, sensores):
        fatos_derivados = set()
        for condicao, acao in self.regras:
            if condicao(sensores):
                fatos_derivados.add(acao)
        return fatos_derivados
def configurar_bc_robo():
    bc = BaseConhecimento()
    bc.adicionar_regra(lambda sensores: sensores['bateria_alta'], 'coleta_permitida')
    bc.adicionar_regra(lambda sensores: sensores['carga_cheia'], 'precisa_descarregar')
    bc.adicionar_regra(lambda sensores: not sensores['bateria_alta'], 'precisa_recarregar')
    #bc.adicionar_regra(lambda bateria: bateria <= 30, 'precisa_recarregar')
    return bc