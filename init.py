from tkinter import *
from tkinter import ttk
import tkinter as tk
from time import strftime


root = tk.Tk()
root.geometry("500x500")
root.title("Checklist")
# Variaveis
text_var = tk.StringVar()
text_var.set("CHECKLIST DE ZEBRA")
Checkbutton1 = IntVar()

def addImpressora():
    newPrint = Toplevel(root)
    newPrint.geometry("300x300")
    newPrint.title("ZEBRA")

    # SELECIONAR FABRICA
    selFabrica = {" Rio Amazonas" : 1,
                "   Rio São Francisco" : 2,
                "   Rio da Prata" : 3}
    
    escolhaFabrica = StringVar(newPrint, '1')

    for (text, value) in selFabrica.items():
        Radiobutton(newPrint, text = text, variable= escolhaFabrica,
                    value= value).pack()

#Menu
menuBar = Menu(root)

Arquivo = Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label="Arquivo", menu = Arquivo)
Arquivo.add_command(label="Adicionar impressora zebra", command = addImpressora)






Quadrado = tk.Label(root,
                 textvariable=text_var,
                 anchor=tk.CENTER,
                 height=3,
                 width=30,
                 bd=3,
                 font=("Arial", 16, "bold"),
                 cursor="hand2",
                 bg='lightblue')



fabrica1 = Checkbutton(root,
                      variable=Checkbutton1,
                      text='Rio Amazonas',
                      onvalue=1,
                      offvalue=0,)





button = tk.Button(root,
                   text="IMPRIMIR",
                   padx=10,
                   pady=5,
                   )



# label text for title 
ttk.Label(root, text = "GFG Combobox Widget",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15))
  
# label 
ttk.Label(root, text = "Select the Month :", 
          font = ("Times New Roman", 10)) 
  
# Combobox creation 
n = tk.StringVar() 
monthchoosen = ttk.Combobox(root, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June', 
                          ' July', 
                          ' August', 
                          ' September', 
                          ' October', 
                          ' November', 
                          ' December') 
  
monthchoosen.pack()


root.config(menu = menuBar) 
Quadrado.pack(pady=20)
fabrica1.pack()
button.pack(padx=20, pady=20)
root.mainloop()

