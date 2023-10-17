#IP为’127.0.0.1‘，端口为8000的socket服务端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 54188))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('客户端IP：', addr)
    while True:
        data = conn.recv(1024*1024).decode('utf-8')
        if data == 'bye' or data == 'Bye' or data == '再见' or data == '拜拜':
            break
        print('等待数据。。。。。。。')
        print(f"数据接收： {data}")
        data=str(input('请输入要发送的信息>>>'))
        conn.send(str(data).encode('utf-8'))
        print(f'数据已发送： ’{data}')
    conn.close()
    break
print('服务器以关闭')


