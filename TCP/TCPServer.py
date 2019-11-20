from socket import *

# 创建TCP欢迎套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
# 将欢迎套接字绑定到指定端口
serverSocket.bind(('', 8000))
# 开始监听来自客户端的连接请求, 设置最大连接数为1
serverSocket.listen(1)

# 持续监听来自客户端的连接请求
while True:
    # 收到客户端连接请求, 创建连接套接字
    connectionSocket, address = serverSocket.accept()
    # 获取客户端发送的信息
    message = connectionSocket.recv(1024)
    # 将客户端发送的字符串变为大写
    modifiedMessage = message.upper()
    # 向用户发送修改后的字符串
    connectionSocket.send(modifiedMessage)
    # 关闭连接套接字
    connectionSocket.close()