from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen()

print('Server is listening on port 8080...')
while True:
    client_socket, addr = server_socket.accept()
    print(f'Connection from {addr}')

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
    client_socket.close()
    print(f'Connection with {addr} closed')