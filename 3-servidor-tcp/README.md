# Prática 03 — Chat com Sockets TCP e Threads

## 1. Objetivo

Desenvolver um sistema de chat utilizando comunicação TCP com Sockets e Threads, permitindo que vários clientes se conectem ao servidor, consultem contatos e enviem mensagens entre si.

## 2. Conceitos

* Socket
* IPv4
* TCP
* Thread
* `bind()`
* `listen()`
* `accept()`
* `connect()`
* `send()`
* `recv()`

## 3. Fluxo

### 3.1 server-chat.py

* cria um socket TCP com IPv4
* associa o IP e a porta informados
* aguarda conexões de clientes
* cria uma Thread para cada cliente conectado
* solicita e valida o nome do cliente
* armazena os clientes conectados em um dicionário
* disponibiliza a lista de contatos
* encaminha mensagens para contatos específicos
* remove o cliente do dicionário ao desconectar

### 3.2 client-chat.py

* cria um socket TCP com IPv4
* conecta-se ao servidor
* solicita o nome do usuário
* permite consultar a lista de contatos usando `/lista`
* permite enviar mensagens usando `/contato <nome> <mensagem>`
* recebe a confirmação de envio do servidor
* mantém a conexão aberta para realizar novas operações

## 4. Comandos

* `/lista` — exibe os contatos conectados.
* `/contato <nome> <mensagem>` — envia uma mensagem para um contato específico.
