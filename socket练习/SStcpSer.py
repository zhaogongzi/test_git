from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime                     #导入相关类

HOST = ''
PORT = 9999
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):              #调用类处理接受到的信息
    def handle(self):                     #重写该类的handle方法
        print('...connected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (
            ctime(), self.rfile.readline().decode()      )).encode() )
        


tcpServ = TCP(ADDR, MyRequestHandler)     #创建了tcp服务器 
print('waiting for connection...')
tcpServ.serve_forever()                   #无限循环
