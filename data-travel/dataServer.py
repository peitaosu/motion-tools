import socket
import threading
import time


class dataServer(threading.Thread):

    def __init__(self, serv_host, serv_port, listen_pool):
        super(dataServer, self).__init__()
        self.host = serv_host
        self.port = serv_port
        self.addr = (serv_host, serv_port)
        self.listen_pool = listen_pool
        self.client_list = []

    def run(self):
        server = socket.socket()
        server.bind(self.addr)
        server.listen(self.listen_pool)
        while True:
            conn, addr = server.accept()
            self.client_list.append((conn, addr))
            print 'Client {} connected.'.format(addr)


if __name__ == "__main__":
    print 'server is running....'
    data_server = dataServer('127.0.0.1', 1234, 10)
    data_server.daemon = True
    data_server.start()
    while True:
        print data_server.client_list
        time.sleep(1)
