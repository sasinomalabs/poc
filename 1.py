import socket

s = socket.socket()
s.connect(("nomasec-labs.ngrok.app", 5000))
s.sendall(b"ping")
print(s.recv(4096))
s.close()

print('hello <b>world</b>')
