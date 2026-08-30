from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))
print('Connected to the server on port 8080')

message = 'Hello, Server! I am a client.'

client_socket.sendall(message.encode())
print(f'Sent message to server')

print(f'Waiting for response from server...')
response = client_socket.recv(1024)

# data formatada em dd/mm/yyyy hh:mm:ss
decoded_response = response.decode()
formatted_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(f'Response from server: {decoded_response} at {formatted_date}')

client_socket.close()
print('Connection closed')