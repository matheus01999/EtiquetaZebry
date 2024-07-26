from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
from print import *
from etiqueta import *
from buttons import *
from printer import *
from tkinter import messagebox

localidades = ['Rio Amazonas', 'Rio da Prata', 'Rio São Francisco']

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
    newPrint.geometry("400x550")
    newPrint.title("CADASTRO DE ZEBRA")

    
    nomPrinter = StringVar()
    ipPrinter = StringVar()
    localiPrinter = StringVar()
    setorPrinter = StringVar()
    modeloPrinter = StringVar()
    analistapPrinter = StringVar()
    macPrinter = StringVar()
    hostnamePrinter = StringVar()
    patrimonioPrinter = StringVar()
    serialPrinter = StringVar()

    # ROTULO DA TELA 
    rotulo = tk.Label(newPrint,
                        text="Adicionar Zebra",
                        bd=3,
                        font=("Arial", 16, "bold"),
                        cursor="hand2",bg='gray',width=30, fg='white').place(x=0, y=0)

    # NOME DA IMPRESSORA
    Label(newPrint, text= 'Endereco IP').place(x=15, y=60)
    Entry(newPrint, textvariable=ipPrinter).place(x=15, y=80)
    # IP DA IMPRESSORA
    Label(newPrint, text= 'Z DA IMPRESSORA').place(x=15, y=100)
    Entry(newPrint, textvariable= nomPrinter).place(x=15, y=120)
    # LOCALIDADE
    Label(newPrint, text= 'Localidade').place(x=15, y=140)
    ttk.Combobox(newPrint, values=localidades).place(x=15, y=160)
    # SETOR
    Label(newPrint, text= 'Setor').place(x=15, y=185)
    Entry(newPrint, textvariable= setorPrinter).place(x=15, y=210)
    # MODELO
    Label(newPrint, text= 'Modelo').place(x=15, y=235)
    Entry(newPrint, textvariable= modeloPrinter).place(x=15, y=260)
    # ANALISTA
    Label(newPrint, text= 'Analista').place(x=15, y=285)
    ttk.Combobox(newPrint, values=localidades).place(x=15, y=310)
    # ENDEREÇO MAC
    Label(newPrint, text= 'MAC').place(x=15, y=335)
    Entry(newPrint, textvariable= macPrinter).place(x=15, y=360)
    # HOSTNAME
    Label(newPrint, text= 'Hostname').place(x=15, y=385)
    Entry(newPrint, textvariable= hostnamePrinter).place(x=15, y=410)
    # PATRIMONIO
    Label(newPrint, text= 'Patrimonio').place(x=15, y=435)
    Entry(newPrint, textvariable= patrimonioPrinter).place(x=15, y=460)
    # SERIAL
    Label(newPrint, text= 'Serial').place(x=15, y=485)
    Entry(newPrint, textvariable= serialPrinter).place(x=15, y=510)

    def salvarZebra():
         print('')
         


    #BOTÃO DE SALVAR
    Button(newPrint,text="Salvar").place(x=330, y=450)
                   

   



# BOTÃO DO MENU PREFERENCIAS

def menuPrefencia():
     prefencePrint = Toplevel(root)
     prefencePrint.geometry('400x300')
     prefencePrint.title("Parametros")

     # CADASTRAR ANALISTA
     analistaCad = StringVar()
     Label(prefencePrint, text ='Analista').place(x=15, y=30)
     Entry(prefencePrint, textvariable=analistaCad).place(x=90, y=30)
     def salvarAnalista():
          print()
     Button(prefencePrint, text="Cadastrar").place(x=250, y=30)

     # CADASTRAR LOCALIDADE
     localCad = StringVar()
     Label(prefencePrint, text ='Localidade').place(x=15, y=70)
     Entry(prefencePrint, textvariable=localCad).place(x=90, y=70)
     def salvarLocal():
          print("teste")
     Button(prefencePrint, text="Cadastrar").place(x=250, y=70)








  

# TELA DE CHECKLIST
def telaChecklist():
        if selecionarEstacao.get() != "Selecione uma estação" and Checkbutton1.get() == 15 or Checkbutton1.get() == 30:
              check15 = Toplevel(root)
              check15.geometry("500x500")
              check15.title("CHECKLIST")

              # ROTULO DO PROGRAMA
              text_var = tk.StringVar()
              text_var.set(selecionarEstacao.get())

              rotulo = tk.Label(check15,
                                   textvariable=text_var,
                                   bd=3,
                                   font=("Arial", 16, "bold"),
                                   cursor="hand2",bg='gray', width=40, fg='white').place(x=0, y=0)





              # BUSCAR ZEBRAS DAS FABRICA SLECIONADA
              rows = cursor.execute("""SELECT * FROM printers
                                          WHERE localidade = '"""+selecionarEstacao.get()+"""'""").fetchall()
              zebras = ['Selecione uma zebra']
              x = len(rows)
              i = 0 
              while i < x:
                    z = rows[i]
                    zebras.append(z[1])
                    i+=1
              


              
              #  GERAR BOTÃO PARA IMPRESSÃO PADRÃO PELA FABRICA SELECIONADA
              
              etiquetaPadraoB = tk.Button(check15, text='Padrão ' + selecionarEstacao.get()).place(x=350, y=450)     



              # SELECIONAR IMPRESSORA 

              zebraSelecionada = StringVar()
              printer_automacao = Checkbutton(check15,
                                   variable=zebraSelecionada,
                                   text='Automacao',
                                   onvalue='automacao',
                                   offvalue=0,).place(y=75, x=400)
              

              Label(check15, text="IP: ").place(y=50, x=15)
              printerEntry = tk.Entry(check15, textvariable=zebraSelecionada).place(y=75, x=15)
              

              ttk.Label(root, text= "Selecionar: ")
              

              Label(check15, text="Selecionar Zebra: ").place(y=50, x=15)
              ttk.Combobox(check15,values=zebras, textvariable=zebraSelecionada).place(y=75 ,x=15)



              #MOSTRAR INFORMAÇÕES DA ZEBRA SELECIONADA
              def pesquisarZebra():
                    if zebraSelecionada.get() != 'Selecione uma zebra':
                     rowsZebra = cursor.execute("""SELECT * FROM printers
                     WHERE nome = '"""+zebraSelecionada.get()+"""'""").fetchall()
                     zebra = rowsZebra[0]
                     

                     Label(check15, text="FILA : " + zebra[1].upper(), font=("Arial", 10, "bold")).place(y=100, x=15)
                     Label(check15, text="IP : " + zebra[2].upper(), font=("Arial", 10, "bold")).place(y=120, x=15)
                     Label(check15, text="LOCALIDADE : " + zebra[3].upper(), font=("Arial", 10, "bold")).place(y=140, x=15)
                     Label(check15, text="ANALISTA : " + zebra[6].upper(), font=("Arial", 10, "bold")).place(y=160, x=15)
                     Label(check15, text="MODELO : " + zebra[5].upper(), font=("Arial", 10, "bold")).place(y=180, x=15)
                     Label(check15, text="SETOR : " + zebra[4].upper(), font=("Arial", 10, "bold")).place(y=200, x=15)
                     Label(check15, text=date.today(), font=("Arial", 15)).place(y=300, x=15)
                     # ENVIAR INFORMAÇÕES PARA ETIQUETA
                     Button(check15, text='Imprimir', command=lambda:gerarEtiqueta(zebra[1],zebra[4],zebra[3], str(date.today()))).place(x=10, y=450)

                     
                    else:
                         messagebox.showwarning("Erro", "Favor Selecionar uma zebra") 

                         

              applyButton = tk.Button(check15, text='Procurar',command=lambda:pesquisarZebra()).place(y=75, x=255)

               
                    


        else:
         messagebox.showwarning("Erro", "Fabrica ou Data não selecionada") 
               
        



              

#Menu
menuBar = Menu(root)
Arquivo = Menu(menuBar, tearoff= 0)
# MENU ARQUIVO 
menuBar.add_cascade(label="Arquivo", menu = Arquivo)
Arquivo.add_command(label="Adicionar impressora zebra", command = menuAdicionarPrinter)
Arquivo.add_command(label="Preferencias", command=menuPrefencia)

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

