def obter_cotacoes_fixas():
  cotacoes = {
    'Real (BRL)': 1.00,
    'Dólar (USD)': 5.00,
    'Euro (EUR)': 5.50,
    'Libra (GBP)': 6.50,
    'Iene (JPY)': 0.035,
    'Dólar Australiano (AUD)': 3.30
  }
  return cotacoes

def calcular_conversao(valor, moeda_origem, moeda_destino, dicionario_cotacoes):
  cotacao_origem = dicionario_cotacoes[moeda_origem]
  cotacao_destino = dicionario_cotacoes[moeda_destino]
  return (valor * cotacao_origem) / cotacao_destino
