import sqlite3
conn = sqlite3.connect("impressoras.db")
cursor = conn.cursor()

a = cursor.execute("""SELECT * FROM printers
                                          WHERE localidade = 'Rio Amazonas'""").fetchall()


 
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []

indice = 1

for i,num in enumerate(a):
    variavel = 'a' + str(indice)
    vars()[variavel].append(num)

    indice = indice + 1
    if (indice >5):
        indice = 1

print(a1)
print(a2)
print(a3)
