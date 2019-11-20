# UDPClient.py
from socket import *
# 创建UDP套接字
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 要发送的信息
message = 'text'
# 目标地址
ipaddress = 'localhost'
# 服务器UDP套接字绑定的接口
port = 8000

# 将信息发送到服务器
clientSocket.sendto(message.encode(), (ipaddress, port))
# 接收服务器的回传信息
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 关闭套接字
clientSocket.close()

# 显示信息
print(modifiedMessage.decode())