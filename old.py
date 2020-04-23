#!/usr/bin/python
# -*- coding: utf-8 -*-

## No Python 2, em vez da função input(), utilizamos a função raw_input() para pegar a entrada do usuário como string
## AF_INET -> IPv4, AF_INET6 -> IPv6 
## SOCK_STREAM -> TCP, SOCK_DGRAM -> UDP

## Imports



## Funções

# def foreheadDoor():
#    print("Testar porta...")
#    ip = input("IP : ")
#    door = int(input("Porta : "))
#    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    if mysocket.connect_ex((ip, door)):
#        print("IP {0}, Porta {1} está fechada !")
#    else:
#        print("IP {0}, Porta {1} está aberta !")