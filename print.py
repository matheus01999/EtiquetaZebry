import socket              
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         


def imprimirEtiqueta(host, port):    
    mysocket.connect((host, port)) #connecting to host
    mysocket.send(b"^XA^A0N,50,50^FO50,50^FDSocket Test^FS^XZ")#using bytes
    mysocket.close () #closing connection



def fakeImpressao(host, port, etiqueta):
    print(etiqueta)


