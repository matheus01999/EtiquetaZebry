import socket              
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
#host = "172.26.51.59" 
#port = 9100 


lerArquivo = open('etiqueta.txt', 'rb')
etiqueta = lerArquivo.read()

def imprimir(host, port):         
    mysocket.connect((host, port)) #connecting to host
    mysocket.send(etiqueta)#using bytes
    mysocket.close () #closing connection


def fakeImpressao(host, port):
    print(host)
    print(port)

