
from socket import *

HOST = '127.0.0.1'         #服务器主机号
PORT = 9999              #服务器端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print (data.decode('utf-8') )

tcpCliSock.close()
