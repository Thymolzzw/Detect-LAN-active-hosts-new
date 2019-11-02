# Detect-LAN-active-hosts
 Detect LAN active hosts


    1、程序的主函数。程序调用socket包的gethostname方法，获得主机名，再根据获得的主机名通过socket.gethostbyname()方法获得主机的IP地址。子网掩码则使用自定义函数getYan(ip)获得。通过自定义类GETIP的getIP()方法获得主机所在网络的所有可用的 IP地址列表。获得IP列表后使用multiprocessing.Process()开10个进程。
    
    2、函数中每个进程的任务由work函数决定，work()函数根据传进的参数列表IPS不同执行不同的任务。首先新建一个socket对象，再遍历IPS，使本机与每一个IP进行连接（connect()方法），如果连接失败则抛出异常（socket.error），如果成功则不抛出异常。每次连接的成功与否都记录在一个TXT文件中（ans.txt）。因为涉及到多进程对同一个文件ans.txt的读写，所以需要一把锁lock，实现临界资源的保护。
    
    3、函数getYan()实现获得本机的子网掩码。首先调用getConfig()方法，该方法通过调动系统命令ipconfig /all将结果存在一个TXT文件（ipconfig.txt）中，在根据本机IP对文本中每行进行分析，得到子网掩码后返回。
    
    4、自定义类GETIP的getIP方法。该方法通过本机IP、子网掩码、网络号的关系进行数学计算，获得本网络中的其他IP地址。首先将IP地址转换成32位的2进制，再计算出网络号与主机号的位数，最后主机号与网络号拼接成一个完整的IP地址。
    
    5、通过遍历ans.txt的每一行计算出所有连接成功的IP地址个数和总数。

