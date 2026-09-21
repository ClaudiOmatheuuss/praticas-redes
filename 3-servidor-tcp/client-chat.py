from socket import socket, AF_INET, SOCK_STREAM


class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        while True:
            message = input('Digite o seu nome: ')
            if message:
                self.client_socket.send(message.encode())
                break

            received_message = self.client_socket.recv(1024).decode()
            if received_message == 'NOME_USADO':
                print('Nome já utilizado. Tente novamente.')

    # ler comandos do usuario /lista para lista de contatos
    # /contato <nome> <mensagem> para enviar mensagem
    def run(self):
        while True:
            command = input('Digite um comando (/lista ou /contato <nome> <mensagem>): ')
            if command == '/lista':
                self.get_contacts()
            elif command.startswith('/contato'):
                parts = command.split(' ', 2)  # split em 3 partes: /contato (0), nome (1), mensagem (2)
                if len(parts) < 3:
                    print('Comando inválido. Use: /contato <nome> <mensagem>')
                    continue
                contact, message = parts[1], parts[2]
                self.send_message(contact, message)
            else:
                print('Comando inválido. Use /lista ou /contato <nome> <mensagem>.')

    # pedir lista de contatos
    def get_contacts(self):
        self.client_socket.send('GET_CONTACTS'.encode())
        contacts = self.client_socket.recv(1024).decode()
        for i, contact in enumerate(contacts.split(',')):
            print(f'Contato {i + 1}: {contact}')

    # enviar mensagem para um contato específico
    def send_message(self, contact: str, message: str):
        try:
            self.client_socket.send(f'SEND_MESSAGE:{contact}:{message}'.encode())
            response = self.client_socket.recv(1024).decode()
            if response == 'MESSAGE_SENT':
                print('Mensagem enviada com sucesso.')
            elif response == 'CONTACT_NOT_FOUND':
                print('Contato não encontrado. Verifique o nome e tente novamente.')
            else:
                print('O servidor não confirmou o envio da mensagem. Problema desconhecido.')

        except Exception as e:
            print(f'Erro ao enviar a mensagem: {e}')
        
    def close(self):
        self.client_socket.close()