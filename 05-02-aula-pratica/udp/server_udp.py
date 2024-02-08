import socket

UDP_IP = ""
UDP_PORT = 5005

sock = socket.socket(
    socket.AF_INET,  # Internet
    socket.SOCK_DGRAM,
)  # UDP
sock.bind((UDP_IP, UDP_PORT))

print("entrei no while")
data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
print(addr)
print("received message: %s" % data)
data = b" received"
IP = addr[0]
PORT = addr[1]
sock.sendto(data, (IP, PORT))
