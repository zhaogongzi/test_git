from socket import *
from time import ctime

HOST = ''
PORT = 49665
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
        tcpCliSock.send('[%s] %s' %(
            bytes(ctime(), 'utf-8'), data))

    tcpCliSock.close()
tcpSerSock.close()
    
                        

