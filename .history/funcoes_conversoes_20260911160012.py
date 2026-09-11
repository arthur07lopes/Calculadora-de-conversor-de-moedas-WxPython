def obter_cotacoes_fixas():
  cotacoes = {
    'Real brasileiro': 1.00,
    'Dólar americano': 5.00,
    'Euro': 5.50,
    'Libra': 6.50,
    'Iene': 0.035,
    'Dólar Australiano': 3.30
  }
  return cotacoes

def calcular_conversao(valor, moeda_origem, moeda_destino, dicionario_cotacoes):
  cotacao_origem = dicionario_cotacoes[moeda_origem]
  cotacao_destino = dicionario_cotacoes[moeda_destino]
  return (valor * cotacao_origem) / cotacao_destino
