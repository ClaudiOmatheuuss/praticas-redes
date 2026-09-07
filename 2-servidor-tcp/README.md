**# Prática 02 — Sockets TCP com Threads**

**## 1. Objetivo**

Aprimorar a comunicação TCP utilizando Threads, permitindo que o servidor atenda múltiplos clientes e que cada cliente envie várias mensagens.

**## 2. Conceitos**

- Socket

- IPv4

- TCP

- Thread

- bind()

- listen()

- accept()

- recv()

- sendall()

**## 3. Fluxo**

**### 3.1 server.py**

- cria socket TCP com IPv4

- associa o IP `0.0.0.0` e porta `8080`

- espera por conexões

- aceita conexão

- cria uma Thread para cada cliente

- recebe e decodifica as mensagens

- envia uma resposta para o cliente

- mantém a conexão aberta para receber novas mensagens

- continua esperando novos clientes

**### 3.2 client.py**

- cria socket TCP com IPv4

- conecta ao servidor pelo IP `127.0.0.1` e porta `8080`

- permite que o usuário digite mensagens

- envia as mensagens codificadas

- espera pela resposta do servidor

- decodifica a resposta

- exibe a resposta junto com a data e hora

- continua enviando mensagens enquanto a conexão estiver aberta
