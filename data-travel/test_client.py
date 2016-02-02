from socket import *

host = '127.0.0.1'
port = 1234
bufsize = 1024
addr = (host, port)

client = socket(AF_INET, SOCK_STREAM)
client.connect(addr)

while True:
    data = client.recv(bufsize)
    if not data:
        break
    print data.strip()
client.close()