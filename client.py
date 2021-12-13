import socket
import threading

ip = '127.0.0.1'
port = 7001
buffer = 2048
nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

def receive():
    while True:
        try:
            message = client.recv(buffer).decode('utf-8')
            if message == 'Name':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))     

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
#dsasdasasdaa
