ERROS!!!
#!/usr/bin/python
# -*- coding: utf-8 -*-


## Imports
import socket


## Funções


def keep():
    while True:
       try:
            b = int(input("digite 0 para cancelar e 1 para continuar : "))
            if b < 2:
                break
            print("caracter inválido")
        except:
            print("caracter inválido")
    return b

def sendMsg():
    print("Conectando...")
    ip = input("IP : ")
    if ip == "":
        ip = "127.0.0.1"
    try:
        door = int(input("Porta : "))
    except:
        door = 12345
   
    print("conectando...")
    try:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysocket.bind((ip, door))
        mysocket.listen(1)
        connection, address = mysocket.accept()
        print("Conectado com",address)
       
    except:
        print("conexão não estabelecida")
    mysocket.close()
        
            
            
# Main
sendMsg()
while True:
    msg = input("Mensagem : ")
    connection.send(msg.encode('ascii'))
    b = keep()
    if b == 0:
        break
connection.close()