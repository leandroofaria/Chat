import socket as sock
import threading

# Lista para armazenar os sockets e nomes dos clientes conectados
clientes = []

def broadcast(mensagem, remetente=None):
    """Envia mensagens para todos os clientes conectados, exceto o remetente."""
    for cliente, _ in clientes:
        if cliente != remetente:
            try:
                cliente.sendall(mensagem.encode())
            except:
                cliente.close()
                remover_cliente(cliente)

def unicast(mensagem, destinatario, remetente_nome):
    """Envia mensagem para um único cliente."""
    for cliente, nome in clientes:
        if nome == destinatario:
            try:
                cliente.sendall(f"{remetente_nome} (privado): {mensagem}".encode())
                return True
            except:
                cliente.close()
                remover_cliente(cliente)
                return False
    return False

def remover_cliente(cliente_socket):
    """Remove um cliente desconectado da lista."""
    for cliente, nome in clientes:
        if cliente == cliente_socket:
            clientes.remove((cliente, nome))
            broadcast(f"{nome} saiu do chat.")
            break

def receber_dados(sock_conn, endereco):
    """Recebe mensagens de um cliente e gerencia sua comunicação."""
    try:
        # Loop para validar o nome do cliente
        while True:
            nome = sock_conn.recv(50).decode().strip()
            if " " in nome:
                sock_conn.sendall("Erro: O nome não pode conter espaços. Use '_' ou tudo junto.".encode())
            else:
                break  # Nome válido, sai do loop

        print(f"Conexão com sucesso com {nome} : {endereco}")
        
        # Adicionar o cliente à lista
        clientes.append((sock_conn, nome))
        
        # Notificar todos os clientes sobre a entrada
        broadcast(f"{nome} entrou no chat.")
        
        while True:
            mensagem = sock_conn.recv(1024).decode()
            print(f"{nome} >> {mensagem}")

            if mensagem.startswith("@"):
                # Mensagem privada
                try:
                    # Identificar destinatário e conteúdo
                    primeiro_espaco = mensagem.find(" ")
                    if primeiro_espaco == -1:
                        sock_conn.sendall("Formato inválido. Use: @nome mensagem".encode())
                        continue
                    
                    destinatario = mensagem[1:primeiro_espaco]
                    conteudo = mensagem[primeiro_espaco + 1:]

                    if not conteudo.strip():
                        sock_conn.sendall("Erro: Mensagem vazia. Use: @nome mensagem".encode())
                        continue

                    sucesso = unicast(conteudo, destinatario, nome)
                    if not sucesso:
                        sock_conn.sendall("Usuário não encontrado.".encode())
                except Exception as e:
                    print(f"Erro no unicast: {e}")
                    sock_conn.sendall("Erro ao enviar mensagem privada.".encode())
            else:
                # Mensagem pública
                broadcast(f"{nome}: {mensagem}", sock_conn)
    except:
        # Caso ocorra erro ou o cliente desconecte
        print(f"Erro ou desconexão do cliente: {endereco}")
        remover_cliente(sock_conn)
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
