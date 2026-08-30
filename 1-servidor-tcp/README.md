# Prática 01 — Sockets TCP

## 1. Objetivo
Criar um servidor utilizando o protocolo de comunicação TCP com Python.

## 2. Conceitos
- Socket
- IPv4
- TCP
- bind()
- listen()
- accept()
- recv()
- sendall()

## 3. Fluxo

### 3.1 server.py
- cria socket tcp com IPV4
- associa o ip '0.0.0.0' e porta 8080, isto é, qualquer interface de rede pode se conectar ao servidor através da porta 8080
- espera conexão
- aceita conexão
- recebe mensagem e decodifica
- envia resposta
- encerra conexão
- espera próxima conexão

### 3.2 client.py
- cria socket tcp com IPV4
- associa o ip na rede local
- envia mensagem codificada
- espera resposta
- decodifica resposta
- fecha o socket