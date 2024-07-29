from print import *
import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   

def gerarEtiqueta(zebra, setor, localidade, data):
    etiqueta = b'''^XA
    ^FO,1^GB700,678,2^FS
    ^CF0,60
    ^FO80,25^FDCHECKLIST ZEBRA^FS
    ^FO0,85^GB700,3,3^FS
    ^CF0,35
    ^FO30,120^FDAnalista : Matheus Rocha ^FS
    ^FO30,180^FDZebra : ^FS
    ^FO30,245^FDSetor :^FS
    ^FO140,245^FD'^FS
    ^FO30,315^FDLocalidade :^FS
    ^FO200,315^FD ^FS
    ^FO30,380^FDData:'''+data+'''^FS
    ^FO120,380^FD hoje^FS
    ^FO0,455^GB700,3,3^FS
    ^FX Third section with bar code.
    ^fo070,470^by2^bcn,150,n
    ^fd>;>817270201>610Z2LT05>59205000123>65^fs
    ^fo120,630^a0n,30,30
    ^fd(17)270201(10)Z2LT05(92)050001235^fs
    ^XZ'''.encode('utf-8')


    print(etiqueta)



def gerarTiquetaPadrao():
    etiquetaPadrao = '''^XA
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
    print(etiquetaPadrao)



   


