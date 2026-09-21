from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def handle_client(client_socket, addr):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                client_socket.close()
                continue

            decoded_data = data.decode()
            print(f'Received message from client ({addr}): {decoded_data}')

            # Send a response back to the client
            response = 'Hi Client! I received your message.'
            client_socket.sendall(response.encode())

            print(f'Sent response to client ({addr})')
        except Exception as e:
            print(f'Error handling client ({addr}): {e}.')
            client_socket.close()
            break

def run_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen()

    print('Server is listening on port 8080...')
    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connection from {addr}')

        #handle the client connection in a separate function
        t = Thread(target=handle_client, args=(client_socket, addr))
        t.start()

if __name__ == '__main__':
    run_server()