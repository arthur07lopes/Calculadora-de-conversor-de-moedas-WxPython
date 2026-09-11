def obter_cotacoes_fixas():
  cotacoes = {
    'Real Brasileiro': 1.00,
    'Dólar Americano': 5.00,
    'Euro': 5.50,
    'Libras Esterlinas': 6.50,
    'Iene Japonês': 0.035,
    'Dólar Australiano': 3.30
  }
  return cotacoes

def calcular_conversao(valor, moeda_origem, moeda_destino, dicionario_cotacoes):
  cotacao_origem = dicionario_cotacoes[moeda_origem]
  cotacao_destino = dicionario_cotacoes[moeda_destino]
  return (valor * cotacao_origem) / cotacao_destino
