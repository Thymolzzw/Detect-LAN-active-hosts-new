
# 该类根据IP地址与子网掩码获得所在局域网内所有的IP地址
class GETIP():

    def __init__(self, IP, Yan):
        self.IP = IP
        self.Yan = Yan

    def getIP(self):
        IP_S = self.IP.split(".")
        Yan = self.Yan.split(".")
        yan_all = ""
        for yan in Yan:
            yan_all += "{:08b}".format(int(yan))
        num_1 = yan_all.count("1")

        ok = True
        if num_1 == 32:
            print("掩码错误！1")
            ok = False
        elif num_1 == 0:
            print("掩码错误！2")
            ok = False
        else:
            if yan_all.count("1"*num_1) != 0:
                print("掩码正确！")
                ok = True
            else:
                print("掩码错误！3")
                ok = False
        ips = []
        if ok:
            ip_all = ""
            for ip_s in IP_S:
                ip_all += "{:08b}".format(int(ip_s))

            ip_sub = ip_all[0:num_1]

            num_0 = 32 - num_1

            for i in range(1, (1 << num_0) - 1):
                ss = "{:0" + str(num_0) + "b}"
                sub_ip = ss.format(i)
                ip = ip_sub + sub_ip
                ip_int = "" + str(int(ip[0:8], 2)) \
                         + "." + str(int(ip[8:16], 2)) \
                         + "." + str(int(ip[16:24], 2)) \
                         + "." + str(int(ip[24:32], 2))
                if ip_int != self.IP:
                    ips.append(ip_int)
        return ips







































