import socket as sock
import threading

# Lista para armazenar os sockets dos clientes conectados
clientes = []

def broadcast(mensagem, remetente=None):
    """Envia mensagens para todos os clientes conectados, exceto o remetente."""
    for cliente in clientes:
        if cliente != remetente:
            try:
                cliente.sendall(mensagem.encode())
            except:
                cliente.close()
                clientes.remove(cliente)

def receber_dados(sock_conn, endereco):
    """Recebe mensagens de um cliente e gerencia sua comunicação."""
    try:
        # Receber o nome do cliente antes de entrar no loop
        nome = sock_conn.recv(50).decode()
        print(f"Conexão com sucesso com {nome} : {endereco}")
        
        # Adicionar o cliente à lista
        clientes.append(sock_conn)
        
        # Notificar todos os clientes sobre a entrada
        broadcast(f"{nome} entrou no chat.")
        
        while True:
            mensagem = sock_conn.recv(1024).decode()
            print(f"{nome} >> {mensagem}")
            broadcast(f"{nome}: {mensagem}", sock_conn)
    except:
        # Caso ocorra erro ou o cliente desconecte
        print(f"Erro ou desconexão do cliente: {endereco}")
        clientes.remove(sock_conn)
        sock_conn.close()

HOST = '26.253.198.232'  # IP do servidor
PORTA = 9999

# Criamos o socket do servidor
socket_server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
# Fazemos o BIND
socket_server.bind((HOST, PORTA))
# Entramos no modo escuta (LISTEN)
socket_server.listen()
print(f"O servidor {HOST}:{PORTA} está aguardando conexões...")

# Loop principal para recebimento de clientes
while True:
    sock_conn, ender = socket_server.accept()
    # Nesse ponto temos uma conexão com um cliente
    # Criamos uma thread para lidar com o cliente
    thread_cliente = threading.Thread(target=receber_dados, args=(sock_conn, ender))
    thread_cliente.start()
