from SocketServer import ThreadingTCPServer, StreamRequestHandler


class dataServer(StreamRequestHandler):

    def handle(self):
        while True:
            data = raw_input()
            if not data:
                break
            self.request.send(data)

if __name__ == "__main__":
    print 'server is running....'
    host = '127.0.0.1'
    port = 1234
    addr = (host, port)
    server = ThreadingTCPServer(addr, dataServer)
    server.serve_forever()
