# Conversor de moedas escrito em WXPython
# Aceita diversos formatos de moeda, incluindo dólares americanos / australianos, euros, libras esterlinas, ienes japoneses e reais brasileiros.

import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        # Mapeia as siglas das moedas para seus nomes em português
        self.moedas = {
            "USD": "Dólar Americano",
            "AUD": "Dólar Australiano",
            "EUR": "Euro",
            "GBP": "Libras Esterlinas",
            "JPY": "Iene Japonês",
            "BRL": "Real Brasileiro"
        }
        self.init_UI()

    def init_UI(self):
        panel = wx.Panel(self)
        # O programa inclui quatro itens principais: primeiro, a combobox da moeda de origem, depois a combobox da moeda de destino, em seguida o campo de entrada para o valor a ser convertido e, por fim, o botão converter.
        sizer = wx.BoxSizer(wx.VERTICAL)
        # Combobox para a moeda de origem
        lbl_origem = wx.StaticText(panel, label="Moeda de origem:")
        self.cb_origem = wx.ComboBox(panel, choices=list(self.moedas.values()), style=wx.CB_READONLY)
        lbl_destino = wx.StaticText(panel, label="Moeda de destino:")
        self.cb_destino = wx.ComboBox(panel, choices=list(self.moedas.keys()), style=wx.CB_READONLY)
        sizer.Add(lbl_origem, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.cb_origem, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(lbl_destino, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.cb_destino, 0, wx.ALL | wx.EXPAND, 5)
        # Campo de entrada para o valor a ser convertido
        lbl_valor = wx.StaticText(panel, label="Valor a ser convertido:")
        self.txt_valor = wx.TextCtrl(panel)
        sizer.Add(lbl_valor, 0, wx.ALL | wx.EXPAND, 5)
        sizer.Add(self.txt_valor, 0, wx.ALL | wx.EXPAND, 5)
        # Botão para realizar a conversão
        btn_converter = wx.Button(panel, label="Converter")
        btn_converter.Bind(wx.EVT_BUTTON, self.on_converter)
        sizer.Add(btn_converter, 0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(sizer)

    def on_converter(self, event):
        origem = self.cb_origem.GetValue()
        destino = self.cb_destino.GetValue()
        valor = self.txt_valor.GetValue()

        if not origem or not destino or not valor:
            wx.MessageBox("Por favor, preencha todos os campos.", "Erro", wx.OK | wx.ICON_ERROR)
            return

        try:
            valor = float(valor)
        except ValueError:
            wx.MessageBox("Por favor, insira um valor numérico válido.", "Erro", wx.OK | wx.ICON_ERROR)
            return

app = wx.App()
frame = MainFrame(None, "Conversor de moedas")
frame.Show()
app.MainLoop()