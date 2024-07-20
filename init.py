from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from print import *
from etiqueta import *


#CONECTANDO COM O BANCO DE DADOS
conn = sqlite3.connect("impressoras.db")
cursor = conn.cursor()
   
    

# DEFINIÇÃO DO LAYOUT INICIAL 
root = tk.Tk()
root.geometry("500x300")
root.title("IMORESSÃO DE CHECKLIST")

#  ARQUIVO - ADICIONAR IMPRESSORA
def addImpressora():
    newPrint = Toplevel(root)
    newPrint.geometry("300x300")
    newPrint.title("ZEBRA")

    namePrint_var=tk.StringVar()
    hostPrint_var=tk.StringVar()
    

    # ADICIONAR IMPRESSORA
    def addPrinter(host, ip):
        # Conectando ao banco de dados existente
        conn = sqlite3.connect('impressoras.db')

        # Inserindo um novo usuário na tabela
        conn.execute("INSERT INTO printers VALUES ('"+host+"', '"+ip+"')")
        conn.commit()


    # IP DA IMPRESSORA
    hostPrint_label = tk.Label(newPrint, text= 'DIGITE O IP DA IMPRESSORA')
    hostPrint_Entry = tk.Entry(newPrint, textvariable=hostPrint_var)
    # NOME DA IMPRESSORA
    namePrint_label = tk.Label(newPrint, text= 'Z DA IMPRESSORA')
    namePrint_Entry = tk.Entry(newPrint, textvariable= namePrint_var)

    #BOTÃO DE SALVAR
    buttonSavePrint = tk.Button(newPrint,
                   text="Salvar",
                   padx=10,
                   pady=5,
                   command=lambda:addPrinter(hostPrint_var.get() ,namePrint_var.get())
                   )

    hostPrint_label.pack()
    hostPrint_Entry.pack()
    namePrint_label.pack()
    namePrint_Entry.pack()
    buttonSavePrint.pack(padx=20, pady=20)

# LISTAR IMPRESSORAS

def topListImpressora():
        listPrint = Toplevel(root)
        listPrint.geometry("300x300")
        listPrint.title("ZEBRA")

        def item(zebra):
            listTeste = tk.Label(listPrint, text= rows[i])
            listTeste.pack()

        def pesquisarZebra():
               resultadoPesquisaZebra = tk.Label(listPrint, text="Zebra")

               resultadoPesquisaZebra.pack()
               

        rows = cursor.execute("SELECT * FROM printers").fetchall()
        searchZebra = tk.Label(listPrint, text = 'Zebra', font=('calibre',10, 'bold'))
        entryZebra = tk.Entry(listPrint)
        buttonSearchZebra = tk.Button(listPrint, text="Pesquisar", command=pesquisarZebra)

        

        searchZebra.pack()
        entryZebra.pack(pady=10)
        buttonSearchZebra.pack(pady=10)

      




# TELA DE CHECKLIST 15 

def telaCheck15():
        if selecionarEstacao.get() != "Selecione uma estação" and Checkbutton1.get() == 15:
                    check15 = Toplevel(root)
                    check15.geometry("600x600")
                    check15.title("CHECKLIST - 15")

                    # ROTULO DO PROGRAMA
                    text_var = tk.StringVar()
                    text_var.set(selecionarEstacao.get())

                    rotulo = tk.Label(check15,
                                    textvariable=text_var,
                                    anchor=tk.CENTER,
                                    height=3,
                                    width=30,
                                    bd=3,
                                    font=("Arial", 16, "bold"),
                                    cursor="hand2",
                                    bg='lightblue')

                    rotulo.pack(pady=20)
                    rows = cursor.execute("SELECT nome FROM printers").fetchall()
                    
        else:
               print("Selecione o dia e a fabrica")
               
        



              

#Menu
menuBar = Menu(root)
Arquivo = Menu(menuBar, tearoff= 0)
# MENU ARQUIVO 
menuBar.add_cascade(label="Arquivo", menu = Arquivo)
Arquivo.add_command(label="Adicionar impressora zebra", command = addImpressora)
Arquivo.add_command(label="Zebras Cadastradas", command = topListImpressora)

root.config(menu = menuBar) 






     
          
     


# ROTULO DO PROGRAMA
text_var = tk.StringVar()
text_var.set("CHECKLIST DE ZEBRA")

rotulo = tk.Label(root,
                 textvariable=text_var,
                 anchor=tk.CENTER,
                 height=3,
                 width=30,
                 bd=3,
                 font=("Arial", 16, "bold"),
                 cursor="hand2",
                 bg='lightblue')

rotulo.pack(pady=20)

# SELEÇÃO DE DIA DO CHECK

Checkbutton1 = IntVar()

check15 = Checkbutton(root,
                      variable=Checkbutton1,
                      text='Chalist 15',
                      onvalue=15,
                      offvalue=0,)

check30 = Checkbutton(root,
                      text='Chalist 30',
                      onvalue=30,
                      offvalue=0,)

check15.pack()
check30.pack()

# APLICAR CHECKLIST


buttonApply = tk.Button(root,
                   text="Aplicar",
                   padx=10,
                   pady=5,
                   command=telaCheck15
                   )

buttonApply.pack(padx=20, pady=20)


#SELEÇÃO DE FABRICA

ttk.Label(root, text= "Selecionar: ")
n =tk.StringVar()

selecionarEstacao = ttk.Combobox(root, width=27,
                                 textvariable= n)
selecionarEstacao['values'] = ('Selecione uma estação',
                               'Rio Amazonas',
                               'Rio da Prata',
                               'Rio São Frnacisco')
selecionarEstacao.pack()
selecionarEstacao.current(0)




root.mainloop()

