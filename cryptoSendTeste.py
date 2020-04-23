#!/usr/bin/python
# -*- coding: utf-8 -*-

## No Python 2, em vez da função input(), utilizamos a função raw_input() para pegar a entrada do usuário como string
## AF_INET -> IPv4, AF_INET6 -> IPv6 
## SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP

## Imports
import socket


## Funções

# def foreheadDoor():
#    print("Testar porta...")
#    ip = input("IP : ")
#    door = int(input("Porta : "))
#    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    if mysocket.connect_ex((ip, door)):
#        print("IP {0}, Porta {1} está fechada !")
#    else:
#        print("IP {0}, Porta {1} está aberta !")

def sendMsg():
    print("Enviar mensagem...")
    ip = input("IP : ")
    door = int(input("Porta : "))
    msg = input("Mensagem : ")
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.bind((ip, door))
    mysocket.listen(1)
    while True:
        connection, address = mysocket.accept()
        print("Conectado com",address)
        connection.send(msg.encode('ascii'))
        connection.close()
        b = int(input("digite zero para cancelar : "))
        if b == 0:
            break



# Main

sendMsg()
        
        
