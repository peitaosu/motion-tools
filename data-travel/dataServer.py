from SocketServer import ThreadingTCPServer, StreamRequestHandler


class dataServer():

    def __init__(self, serv_host, serv_port):
        self.host = serv_host
        self.port = serv_port
        self.addr = (serv_host, serv_port)
        self.server = ThreadingTCPServer(self.addr, RequestHandler)
        self.server.serve_forever()


class RequestHandler(StreamRequestHandler):

    def handle(self):
        while True:
            data = raw_input()
            if not data:
                break
            self.request.send(data)

if __name__ == "__main__":
    print 'server is running....'
    data_server = dataServer('127.0.0.1', 1234)
