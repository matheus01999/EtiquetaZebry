from tkinter import *
from etiqueta import *
from datetime import date

class BotaoAmazonas:
 def __init__(self, zebra, setor):
  self.data = str(date.today())
  self.localidade = 'Rio Amazonas'
  self.setor = setor
  self.zebra = zebra
  gerarEtiqueta(self.zebra, self.setor, self.localidade, self.data)
  


    
    

