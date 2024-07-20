from init import *

def telaCheck15():
        check15 = Toplevel(root)
        check15.geometry("400x400")
        check15.title("CHECKLIST - 15")

        #BOTÃO COM O NOME DA IMPRESSORA
        buttonSavePrint = tk.Button(check15,
                   text="Atualizar",
                   padx=10,
                   pady=5,
                   command=lambda:fakeImpressao("172.26.51.59" ,9100)
                   )
        buttonSavePrint.pack(padx=20, pady=20)