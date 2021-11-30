import socket
import threading
from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode, b64decode

ip = '127.0.0.1'
port = 7001
buffer = 1024
nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

#key = Fernet.generate_key()
#f = Fernet(key)
#Ctext = f.encrypt(b"test1234")
data = b"test12345"
key = "3t6v9y$B&E)H@McQ"
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data,AES.block_size))


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
