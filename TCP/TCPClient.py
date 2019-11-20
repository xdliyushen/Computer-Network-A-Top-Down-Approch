from socket import *

# 创建TCP套接字
clientSocket = socket(AF_INET, SOCK_STREAM)
# 指定服务器ip地址
host = '127.0.0.1'
# 服务器TCP套接字绑定的接口
port = 8000
# 要发送的信息
message = 'text'

# 向服务器发起连接
clientSocket.connect((host, port))
# 发送信息
clientSocket.send(message.encode())
# 从服务器接收信息
modifiedMessage = clientSocket.recv(1024)
# 关闭套接字
clientSocket.close()

# 显示信息
print(modifiedMessage.decode())

