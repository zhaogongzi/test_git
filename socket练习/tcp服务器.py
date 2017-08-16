#半工聊天

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 9999
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)      #套接字绑定地址
tcpSerSock.listen(5)       #监听

while True:             #开启tcp监听器的调用
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        
        
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break

        print (data.decode('utf-8') ) #1
        
        #tcpCliSock.send(('[%s] %s' %(
            #ctime(), data)).encode())

        data = input('> ')      #2
        if not data:
            break
        tcpCliSock.send(data.encode())

    tcpCliSock.close()
tcpSerSock.close()
