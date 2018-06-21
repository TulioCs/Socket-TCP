# -*- coding: utf-8 -*-
import socket

#comunicação ipv4 e socket TCP
cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Definindo o IP do servidor
IP = 'localhost'

#Definindo a porta
porta = 5002

#Definindo o tamanho do buffer para as mensagens
buffer_size = 1024

cliente.connect((IP,porta))
menu = cliente.recv(buffer_size)
opcao = raw_input(menu + "\n")

while opcao != '0':
	#Enviando mensagem para o servidor
	cliente.send(opcao)

	#Obtendo resultado enviado pelo servidor
	data = cliente.recv(buffer_size)

	#Obtendo a escolha do cliente
	opcao = raw_input(data + '\n')
cliente.send(opcao)
print(cliente.recv(buffer_size)+'\n')
cliente.close()	

