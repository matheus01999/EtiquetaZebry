import socket    
from etiqueta import *      
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         

queta = b'''^XA
^FO,1^GB700,678,2^FS
^CF0,60
^FO80,25^FDCHECKLIST ZEBRA^FS
^FO0,85^GB700,3,3^FS
^CF0,35
^FO30,120^FDAnalista : Matheus Rocha ^FS
^FO30,180^FDZebra : ZEBRA^FS
^FO30,245^FDSetor :^FS
^FO140,245^FD SETOR^FS
^FO30,315^FDLocalidade :^FS
^FO200,315^FD LOCALIDADE^FS
^FO30,380^FDData:^FS
^FO120,380^FD DATA^FS
^FO0,455^GB700,3,3^FS
^FX Third section with bar code.
^fo070,470^by2^bcn,150,n
^fd>;>817270201>610Z2LT05>59205000123>65^fs
^fo120,630^a0n,30,30
^fd(17)270201(10)Z2LT05(92)050001235^fs
^XZ'''

def imprimirEtiqueta(host, port, etiqueta):    
    mysocket.connect((host, port)) #connecting to host
    mysocket.send(etiqueta)#using bytes
    mysocket.close () #closing connection



def fakeImpressao():
    print('teste')


