from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.clients = {}  # dicionário para armazenar clientes conectados {nome: socket}
        self.start_server()

    def start_server(self):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f'Servidor iniciado em {self.host}:{self.port}')

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f'Cliente conectado de {addr}')
            Thread(target=self.handle_client, args=(client_socket,addr)).start()

    # worker thread para lidar com cada cliente
    def handle_client(self, client_socket, addr):
        # Receber o nome do cliente
        while True:
            name = client_socket.recv(1024).decode()
            if name in self.clients:
                client_socket.send('NOME_USADO'.encode())
            else:
                self.clients[name] = client_socket
                print(f'Cliente {name} conectado de {addr}')
                # client_socket.send('NOME_OK'.encode())
                break

        # recebemos mensagens do cliente em loop
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break

                if message == 'GET_CONTACTS':
                    contacts = ','.join(self.clients.keys())
                    client_socket.send(contacts.encode())
                elif message.startswith('SEND_MESSAGE:'):
                    _, contact, msg = message.split(':', 2)  
                    if contact in self.clients:
                        self.clients[contact].send(f'Mensagem de {name}: {msg}'.encode())
                        client_socket.send('MESSAGE_SENT'.encode())
                    else:
                        client_socket.send('CONTACT_NOT_FOUND'.encode())
                else:
                    print(f'Mensagem recebida de {name}: {message}')

            except Exception as e:
                print(f'Erro ao lidar com o cliente {name}: {e}')
                break

        # cliente desconectado, remover do dicionário e fechar o socket
        print(f'Cliente {name} desconectado')
        del self.clients[name]
        client_socket.close()


if __name__ == '__main__':
    server = Server('0.0.0.0', 8082)