from socket import *

# 构造HTTP报文
def generateHTTPResponse(response_start_line, response_header, response_body):
    return (response_start_line + response_header + '\r\n' + response_body).encode()

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
    # 获取客户端发送的HTTP报文
    http_message = (connectionSocket.recv(1024)).decode()
    
    try:
        # 获取请求的文件路径
        path = http_message.split(' ')[1]
        if (path == '/' or path == '/index.html'):
            # 读取文件
            f = open('C:\\Users\\Admin\\Desktop\\Computer-Network-A-Top-Down-Approch\\HTTP\\index.html')
            output_data = f.read()
            
            # HTTP文件报文
            response_start_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: Web Server\r\n'
            response_body = output_data
        else:
            # 目标路径没有文件, 抛出错误,返回404
            raise Exception('No Such File!')
    except BaseException as e:
        # 404HTTP报文
        # print(e)
        response_start_line = 'HTTP/1.1 404 Not Found\r\n'
        response_header = 'Server: Web Server\r\n'
        response_body = ''

    # 构造HTTP报文
    response = generateHTTPResponse(response_start_line, response_header, response_body)
    # 向用户发送HTTP报文
    connectionSocket.send(response)
    # 关闭连接套接字
    connectionSocket.close()
