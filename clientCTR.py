import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import json

ip = '127.0.0.1'
port = 7001
buffer = 2048
nickname = input("Choose your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

#key = Fernet.generate_key()
#f = Fernet(key)
#Ctext = f.encrypt(b"test1234")
# data = b"test12345"
key = b"3t6v9y$B&E)H@McQ"
key256 = b"G-KaPdSgVkYp3s6v9y$B?E(H+MbQeThW"



def receive():
    while True:
        try:
            message = client.recv(buffer).decode('utf-8')
            if message == 'Name':
                client.send(nickname.encode('utf-8'))
            else:
                b64 = json.loads(message)
                nonce = b64decode(b64['nonce'])
                ct = b64decode(b64['ciphertext'])
                cipher = AES.new(key256, AES.MODE_CTR, nonce=nonce)
                pt = cipher.decrypt(ct).decode('utf-8')
                print(b64['name'] + ": " + json.loads(pt)['data'])
        except Exception as e: pass
def write():
    while True:
        #message = f'{nickname}: {input("")}'
        message = json.dumps({"data":input("")})
        cipher = AES.new(key256, AES.MODE_CTR)
        ct_bytes = cipher.encrypt(message.encode('utf-8'))
        nonce = b64encode(cipher.nonce).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'name' : nickname, 'nonce':nonce, 'ciphertext':ct})
        client.send(result.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
#dsasdasasdaa
