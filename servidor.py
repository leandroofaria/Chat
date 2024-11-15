import socket as sock
import threading

def receber_dados(sock_conn, endereco):
    #Receber o nome antes de entrar no loop
    nome = sock_conn.recv(50).decode()
    print(f"Conexão com sucesso com {nome} : {endereco}")
    while True:
        try:
            mensagem = sock_conn.recv(1024).decode()
            print(f"{nome} >> {mensagem}")
        except:
            print("Erro ao receber mensagem... fechando conexão")
            sock_conn.close()
            return

HOST = '127.0.0.1' #Endereço IP do servidor
PORTA = 9999

#Criamos o socket do servidor
socket_server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
#Fazemos o BIND
socket_server.bind((HOST,PORTA))
#Entramos no modo escuta (LISTEN)
socket_server.listen()
print(f"O servidor {HOST}:{PORTA} está aguardando conexões...")
#Loop principal para recebimento de clientes
while True:
    sock_conn, ender = socket_server.accept()
    #Nesse ponto temos uma conexão com um cliente
    #Vamos fazer um loop para recebimento de dados
    
    #Agora vamos criar Threads para os loops
    thread_cliente = threading.Thread(target=receber_dados, args=[sock_conn, ender])
    thread_cliente.start()


