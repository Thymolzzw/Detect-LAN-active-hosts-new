import socket
import sys

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("服务器主机IP为："+host_ip)
    print("Listening......")
    port = 9999
    server_socket.bind((host_name, port))
    server_socket.listen(5)

    i = 1
    while True:
        clientSocket, addr = server_socket.accept()
        print(addr)
        print("连接地址：%s" % str(addr))
        msg = "欢迎访问，第" + str(i) + "位会员" + '\r\n'
        i += 1
        clientSocket.send(msg.encode('utf-8'))
        clientSocket.close()


if __name__ == '__main__':
    main()

