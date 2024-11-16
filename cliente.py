import socket as sock
import threading

def receber_mensagens(socket_cliente):
    """Recebe mensagens do servidor e exibe no terminal."""
    while True:
        try:
            mensagem = socket_cliente.recv(1024).decode()
            print(mensagem)
        except:
            print("Conexão encerrada pelo servidor.")
            socket_cliente.close()
            break

HOST = '26.253.198.232'  # IP do servidor
PORTA = 9999

# Criamos o socket do cliente
socket_cliente = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

# Conecta ao servidor
socket_cliente.connect((HOST, PORTA))
print(5 * "*" + " INICIANDO CHAT " + 5 * "*")
nome = input("Informe seu nome para entrar no chat:\n")
socket_cliente.sendall(nome.encode())

# Thread para receber mensagens do servidor
thread = threading.Thread(target=receber_mensagens, args=(socket_cliente,))
thread.start()

# Loop para envio de mensagens
while True:
    mensagem = input('')
    if mensagem.lower() == "/sair":
        socket_cliente.sendall(mensagem.encode())  # Envia o comando para o servidor
        print("Você saiu do chat.")
        socket_cliente.close()
        break
    socket_cliente.sendall(mensagem.encode())
