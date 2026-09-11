# Conversor de moedas escrito em WXPython
# Aceita diversos formatos de moeda, incluindo dólares americanos / australianos, euros, libras esterlinas, ienes japoneses e reais brasileiros.

import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        self.init_UI()
        # Mapeia as siglas das moedas para seus nomes em português
        self.moedas = {
            "USD": "Dólar Americano",
            "AUD": "Dólar Australiano",
            "EUR": "Euro",
            "GBP": "Libras Esterlinas",
            "JPY": "Iene Japonês",
            "BRL": "Real Brasileiro"
        }

    def init_UI(self):
        panel = wx.Panel(self)
        # O programa inclui quatro itens principais: primeiro, a combobox da moeda de origem, depois a combobox da moeda de destino, em seguida o campo de entrada para o valor a ser convertido e, por fim, o botão converter.
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Combobox para a moeda de origem