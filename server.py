import socket
import threading

ip = '127.0.0.1'
port = 7001
buffer = 1024

# server start
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip,port))
s.listen()

# lists of clients and their nicknames
clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(buffer)
            broadcast(message)
        except:
            # removes a client from the chat
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left!\n'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        # accepts connection
        client, addr = s.accept()
        print(f"Connected with {str(addr)}")

        # Saves nicknames
        client.send('Name'.encode('utf-8'))
        nickname = client.recv(buffer).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)



        # prints nickname
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!\n".encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
