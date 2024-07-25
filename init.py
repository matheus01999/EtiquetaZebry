from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from print import *
from etiqueta import *
from buttons import *
from tkinter import messagebox



#CONECTANDO COM O BANCO DE DADOS
conn = sqlite3.connect("impressoras.db")
cursor = conn.cursor()
   

# DEFINIÇÃO DO LAYOUT INICIAL 
root = Tk()
root.geometry("500x300")
root.title("IMORESSÃO DE CHECKLIST")


#  TELA PARA ADICIONAR IMPRESSORA
def menuAdicionarPrinter():
    newPrint = Toplevel(root)
    newPrint.geometry("300x200")
    newPrint.title("ZEBRA")
    # IP DA IMPRESSORA
    namePrint_var=tk.StringVar()
    hostPrint_var=tk.StringVar()

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


# BOTÃO DO MENU ADICIONAR IMPRESSORA

def addPrinter(host, ip):
    # INSERIR OS DADOS DA IMPRESSORA NO BANCO
    conn.execute("INSERT INTO printers VALUES ('"+host+"', '"+ip+"')")
    conn.commit()
       

# BOTÃO DO MENU PARA LISTAR IMPRESSORAS

def menuListarPrinter():
        listPrint = Toplevel(root)
        listPrint.geometry("300x300")
        listPrint.title("ZEBRA")

        searchZebra = tk.Label(listPrint, text = 'Zebra', font=('calibre',10, 'bold'))
        entryZebra = tk.Entry(listPrint)
        buttonSearchZebra = tk.Button(listPrint, text="Pesquisar")



        searchZebra.pack()
        entryZebra.pack(pady=10)
        buttonSearchZebra.pack(pady=10)

  

# TELA DE CHECKLIST 15 
def telaChecklist():
        if selecionarEstacao.get() != "Selecione uma estação" and Checkbutton1.get() == 15 or Checkbutton1.get() == 30:
              check15 = Toplevel(root)
              check15.geometry("500x500")
              check15.title("CHECKLIST - 15")

              # ROTULO DO PROGRAMA
              text_var = tk.StringVar()
              text_var.set(selecionarEstacao.get())

              rotulo = tk.Label(check15,
                                   textvariable=text_var,
                                   bd=3,
                                   font=("Arial", 16, "bold"),
                                   cursor="hand2").place(x=10, y=10)





              # BUSCAR ZEBRAS DAS FABRICA SLECIONADA
              rows = cursor.execute("""SELECT * FROM printers
                                          WHERE localidade = '"""+selecionarEstacao.get()+"""'""").fetchall()
              

              
              #  GERAR BOTÃO PARA IMPRESSÃO PADRÃO PELA FABRICA SELECIONADA
              
              etiquetaPadraoB = tk.Button(check15, text='Padrão ' + selecionarEstacao.get()).place(x=350, y=450)     



              # SELECIONAR IMPRESSORA 

              zebraSelecionada = StringVar()
              printer_automacao = Checkbutton(check15,
                                   variable=zebraSelecionada,
                                   text='Automacao',
                                   onvalue='172.26.51.59',
                                   offvalue=0,).place(y=50, x=400)
              

              Label(check15, text="IP: ").place(y=50, x=15)
              printerEntry = tk.Entry(check15, textvariable=zebraSelecionada).place(y=50, x=35)
              botaoImprimir = tk.Button(check15, text='Imprimir').place(x=10, y=470)

              ttk.Label(root, text= "Selecionar: ")


              comboxSelZebra = ttk.Combobox(check15, 
                                          textvariable= zebraSelecionada)
              comboxSelZebra['values'] = ('Selecione uma zebra',
                                          'Rio Amazonas',
                                          'Rio da Prata',
                                          'Rio São Frnacisco')
              comboxSelZebra.place(y=50 ,x=15)
              comboxSelZebra.current(0)

              #MOSTRAR INFORMAÇÕES DA ZEBRA SELECIONADA
              def pesquisarZebra():
                    if zebraSelecionada.get() != 'Selecione uma zebra':
                     rowsZebra = cursor.execute("""SELECT * FROM printers
                     WHERE ip = '"""+zebraSelecionada.get()+"""'""").fetchall()
                     zebra = rowsZebra[0]

                     Label(check15, text="FILA : " + zebra[1]).place(y=100, x=15)
                     Label(check15, text="IP : " + zebra[2]).place(y=120, x=15)
                     Label(check15, text="LOCALIDADE : " + zebra[3]).place(y=140, x=15)
                     Label(check15, text="SETOR: " + zebra[4]).place(y=160, x=15)



                    else:
                         messagebox.showwarning("Erro", "Favor Selecionar uma zebra") 
                         


              applyButton = tk.Button(check15, text='Procurar',command=lambda:pesquisarZebra()).place(y=50, x=170)


              
              

                    
              
                          
              


   



       

              # GERAR BOTOES COM BASE NA QUERY
              a1 = []
              a2 = []
              a3 = []
              a4 = []
              a5 = []

              indice = 1
              listaZebras = []

              for i,num in enumerate(rows):
                     variavel = 'a' + str(indice)
                     vars()[variavel].append(num)
                     listaZebras.append(variavel)

                     indice = indice + 1
                     if (indice >5):
                            indice = 1

              botaozebra1 = a1[0]
              #b1 = BotaoAmazonas(botaozebra1[1], botaozebra1[4])

                     



              
                    


        else:
         messagebox.showwarning("Erro", "Fabrica ou Data não selecionada") 
               
        



              

#Menu
menuBar = Menu(root)
Arquivo = Menu(menuBar, tearoff= 0)
# MENU ARQUIVO 
menuBar.add_cascade(label="Arquivo", menu = Arquivo)
Arquivo.add_command(label="Adicionar impressora zebra", command = menuAdicionarPrinter)
Arquivo.add_command(label="Zebras Cadastradas", command = menuListarPrinter)

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
                      variable=Checkbutton1,
                      onvalue=30,
                      offvalue=0,)

check15.pack()
check30.pack()

# APLICAR CHECKLIST


buttonApply = tk.Button(root,
                   text="Aplicar",
                   padx=10,
                   pady=5,
                   command=telaChecklist
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

