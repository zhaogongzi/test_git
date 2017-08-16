from socket import *

HOST = 'localhost'         #服务器主机号
PORT = 9999              #服务器端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)

#不能再这个执行过程中都保持连接，每次向服务器发送消息时，
#都需要创建一个新的套接字，所以把它放在循环里面
while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(('%s\r\n' % data).encode() ) #必须发送行终止符
    data = tcpCliSock.recv(BUFSIZ).decode()
    if not data:
        break
    print (data.strip())            #处理换行符
    tcpCliSock.close()
