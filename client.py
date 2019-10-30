import socket


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    host_ip = socket.gethostbyname(host)
    port = 9999
    try:
        s.connect((host_ip, port))
    except socket.error:
        print("服务器连接失败！")
    else:
        # 接收小于1024字节的数据
        msg = s.recv(1024)
        s.close()
        print(msg.decode('utf-8'))


if __name__ == '__main__':
    main()

