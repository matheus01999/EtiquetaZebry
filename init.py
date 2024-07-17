from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from time import strftime

root = tk.Tk()
root.geometry("500x500")
root.title("Checklist")
# Variaveis
text_var = tk.StringVar()
text_var.set("CHECKLIST DE ZEBRA")
Checkbutton1 = IntVar()

#Menu
menuBar = Menu(root)

Arquivo = Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label="Arquivo", menu = Arquivo)
Arquivo.add_command(label="Adicionar Impressora", command = None)




label = tk.Label(root,
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

radioFabrica = {"Rio Amazonas" : 1,
                "Rio São Francisco" : 2,
                "Rio da Prata" : 3}



button = tk.Button(root,
                   text="IMPRIMIR",
                   padx=10,
                   pady=5,
                   )

escolhaFabrica = StringVar(root, '1')


for (text, value) in radioFabrica.items():
    Radiobutton(root, text = text, variable= escolhaFabrica,
                value= value).pack()




root.config(menu = menuBar) 
label.pack(pady=20)
fabrica1.pack()
button.pack(padx=20, pady=20)
root.mainloop()

