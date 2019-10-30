import socket
from subprocess import *

def getIpConfig():
    with open("ipconfig.txt", "w") as f:
        p = Popen(['ipconfig', '/all'], stdin=PIPE, stdout=f, shell=True)
        p.wait()

def getYan(IP):
    getIpConfig()
    yan = ""
    context = []
    with open("ipconfig.txt", "r") as f:
        for line in f:
            context.append(line)
    i = 0
    for i in range(len(context)):
        if context[i].count(IP) == 1:
            break
    return context[i+1].split(" ")[-1]
