#IP为’127.0.0.1‘，端口为8000的socket客户端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 54188))

while True:
    data=str(input('请输入要发送的信息>>>'))
    if data == 'bye' or data == 'Bye' or data == '再见' or data == '拜拜':
        s.send(str(data).encode('utf-8'))
        break
    s.send(str(data).encode('utf-8'))
    print(f'’{data}‘数据已发送')
    data = s.recv(1024*1024).decode('utf-8')
    print('等待数据。。。。。。。')
    print(f'数据已接收： ’{data}‘')
s.close()
print('连接以关闭')

