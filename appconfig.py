from socket import socket, AF_INET, SOCK_DGRAM


def send(key):
    s = socket(AF_INET, SOCK_DGRAM)
    key = bytes(key, encoding = "utf8")
    s.sendto(key, ('192.168.31.37', 20000))
    # ret = s.recvfrom(20001)
    # print(ret)
    
if __name__ == "__main__":
    send('a_down')