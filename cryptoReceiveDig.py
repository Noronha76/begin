#!/usr/bin/python


## Imports
import socket


## Funções
def keep():
    while True:
        try:
            b = int(input("digite 0 para cancelar e 1 para continuar : "))
            if b < 2:
                break
            print("caracter inválido!")
        except:
            print("caracter inválido!")
            print("encerrando operação...")
            b = 0
            break
    return b

## Main
print("Receber mensagem...")
ip = input("IP : ")
if ip == "":
    ip = "127.0.0.1"
try:
    door = int(input("Porta : "))
except:
    door = 12345
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((ip, door))
msg = mysocket.recv(10000)
print(msg.decode('ascii'))
while True:
    b = keep()
    if b == 0:
        break
    msg = mysocket.recv(10000)
    print(msg.decode('ascii'))
mysocket.close()    
