from GETIP import GETIP
import socket
import multiprocessing
from getYanMa import *

def main():

    host = socket.gethostname()
    host_ip = socket.gethostbyname(host)
    host_ip = "172.23.103.62"
    print("本机IP：", host_ip)
    port = 135
    lock = multiprocessing.Lock()
    yan = getYan(host_ip)
    print("本机掩码：", yan)
    g = GETIP(IP=host_ip, Yan=yan)
    IPS = g.getIP()
    file = "ans.txt"
    with open(file, "w") as f:
        pass

    IPS_LEN = len(IPS)
    space = IPS_LEN // 10
    p1 = multiprocessing.Process(target=work, args=(IPS[0:space], port, lock, file))
    p2 = multiprocessing.Process(target=work, args=(IPS[space:space*2], port, lock, file))
    p3 = multiprocessing.Process(target=work, args=(IPS[space*2:space*3], port, lock, file))
    p4 = multiprocessing.Process(target=work, args=(IPS[space*3:space*4], port, lock, file))
    p5 = multiprocessing.Process(target=work, args=(IPS[space*4:space*5], port, lock, file))
    p6 = multiprocessing.Process(target=work, args=(IPS[space * 5:space * 6], port, lock, file))
    p7 = multiprocessing.Process(target=work, args=(IPS[space * 6:space * 7], port, lock, file))
    p8 = multiprocessing.Process(target=work, args=(IPS[space * 7:space * 8], port, lock, file))
    p9 = multiprocessing.Process(target=work, args=(IPS[space * 8:space * 9], port, lock, file))
    p10 = multiprocessing.Process(target=work, args=(IPS[space * 9:], port, lock, file))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    print("END!!")

def work(IPS, port, lock, filename):
    for ip in IPS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        line = ""
        try:
            s.settimeout(1)
            s.connect((ip, port))
        except socket.error:
            line += str(ip) + "连接失败！"
            print(ip, "连接失败！")
        else:
            line += str(ip) + "连接成功！"
            print(ip, "连接成功！")
        s.close()
        with lock:
            f = open(filename, "a+")
            f.write(line + "\n")
            f.close()


if __name__ == '__main__':
    main()













