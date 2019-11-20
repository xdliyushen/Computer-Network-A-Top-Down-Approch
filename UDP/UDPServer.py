# UDPServer.py
from socket import *
# 创建UDP套接字
serverSocket = socket(AF_INET, SOCK_DGRAM)
# 将套接字绑定到指定接口
serverSocket.bind(('', 8000))

# 持续接收UDP报文
while True:
    # 接收客户端消息, 获取客户端地址
    message, clientAddress = serverSocket.recvfrom(2048)
    # 将客户端传来的字符串变为大写
    modifiedMessage = message.upper()
    # 将更改后的信息传回给客户端
    serverSocket.sendto(modifiedMessage, clientAddress)