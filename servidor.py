# -*- coding: utf-8 -*-
#coding: utf-8
import socket
import thread

#Definindo o IP do servidor
IP = 'localhost'

#Definindo a porta
porta = 5002

#Definindo o tamanho do buffer para as mensagens
buffer_size = 1024
def get_menu():
    dados = open('catalago.txt')
    menu = ''

    #Percorrendo as linhas do arquivo
    for line in dados:
        #Obtendo as temperaturas e as datas e horas
        x , y = line.split(';')
        #Atribuindo os valores das temperaturas (float) para a lista
        menu += x + '\n'
    dados.close()
    menu += '0-Para Finalizar a Consulta \n' 
    return menu
   
def get_desc(x):
    arquivo = open('catalago.txt') 
    z = arquivo.readlines()
    tam = len(z)
    if (x > 0 and x <= tam):
        l = z[x-1]
        m,d = l.split(';')
        return d
    else:
        return "Opção Inválida \n"
    arquivo.close()

def conectado (conexao, endereco):
    conexao.send(get_menu())
    while True:
        data = conexao.recv(buffer_size)
        if(data != '0'):
            try:
                opcao = int(data)
            except:
                conexao.send("Opção Inválida\n")
            conexao.send(str(get_desc(opcao)))
        else:    
            conexao.send("Desconectado")
            conexao.close()
            thread.exit()

def main():
    #comunicação ipv4 e socket TCP
    servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Configurando o servidor com o IP e a porta definidos anteriormente
    servidor.bind((IP, porta))
    servidor.listen(5)

    while True:
        conexao,endereco = servidor.accept()
        thread.start_new_thread(conectado,tuple([conexao,endereco]))

if __name__ == '__main__':
    main()



