import socket as sock

HOST = '127.0.0.1' #IP DO SERVIDOR
PORTA = 9999 #PORTA DO SERVIDOR

#criamos o socket do cliente
socket_cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

#Solicita conexão ao servidor (HOST,PORTA)
socket_cliente.connect((HOST,PORTA))
#Criamos um loop para envio de dados
print(5*"*" + "INICIANDO CHAT" + 5*"*")
nome = input("Informe seu nome para entrar no chat:\n")
#Antes de entrar no loop enviamos o nome
socket_cliente.sendall(nome.encode())
while True:
    mensagem = input('')
    #encode: faz a conversão str->bytes
    socket_cliente.sendall(mensagem.encode())