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

# ADICIONAR IMPRESSORA


def adicionarImpressora(nome, ip, localidade, setor, modelo, analista, mac, hostname, patrimonio, serial):
    # INSERIR OS DADOS DA IMPRESSORA NO BANCO
    conn.execute("INSERT INTO printers VALUES ('"+nome+"',"+nome+"', '"+ip+"','"+localidade+"','"+setor+"','"+modelo+"','"+analista+"','"+mac+"','"+hostname+"','"+patrimonio+"','"+serial+"')")
    conn.commit()