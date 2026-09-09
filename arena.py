import random

tipos_minerios = [('ouro', 50), ('prata', 30), ('diamante', 100), ('bronze', 10), ('rubi', 80)]

def sortear_posicao(quant, largura, altura, celulas_protegidas):
  posicoes = set()
  while len(posicoes) < quant:
    x = random.randint(0, largura - 1)
    y = random.randint(0, altura - 1)
    if (x, y) not in celulas_protegidas:
      posicoes.add((x, y))
      celulas_protegidas.add((x, y))

  return posicoes

def sortear_minerio(x, y, tipos_minerios):
  tipo, valor = random.choice(tipos_minerios)
  return (x, y, tipo, valor)


def gerar_arena(largura, altura, n_paredes, n_minerios, n_armadilhas, seed=0):
  random.seed(seed)

  posicoes_proibidas = {
    (0,0), (0,1), (1,0),
    (14,8), (14,7), (13,8)
  }

  posicoes_paredes = sortear_posicao(n_paredes, largura, altura, posicoes_proibidas)
  posicoes_armadilhas = sortear_posicao(n_armadilhas, largura, altura, posicoes_proibidas)
  posicoes_minerios = sortear_posicao(n_minerios, largura, altura, posicoes_proibidas)

  minerios = {}

  for (x,y) in posicoes_minerios:
    _,_,tipo, valor = sortear_minerio(x, y, tipos_minerios)
    minerios[(x,y)] = {'tipo': tipo, 'valor': valor}

  for y in range(altura):
    for x in range(largura):
      pos = (x, y)
      if pos == (0, 0):
        print("A", end=" ")
      elif pos in posicoes_paredes:
        print("#", end=" ")
      elif pos in posicoes_armadilhas:
          print("-", end=" ")
      elif pos in minerios:
        # renderizar a inicial do tipo do minério
        inicial = minerios[pos]['tipo'][0]
        print(inicial, end=" ")
      elif pos == (14, 8):
        print("B", end=" ") 
      else:
        print(".", end=" ")
    print()

  return posicoes_paredes, posicoes_armadilhas, minerios
