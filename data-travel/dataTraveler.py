import threading
import Queue
from dataServer import dataServer
from dataProducer import dataProducer
import time


class dataTraveler(threading.Thread):

    def __init__(self, data_queue, client_list):
        super(dataTraveler, self).__init__()
        self.client_list = client_list
        self.data_queue = data_queue

    def run(self):
        while True:
            data = self.data_queue.get()
            for conn, addr in self.client_list:
                try:
                    conn.sendall(data)
                except Exception, (errno, message):
                    if errno == 32:
                        self.client_list.remove((conn, addr))
                        print 'Client {} disconnected.'.format(addr)


if __name__ == "__main__":
    print 'server is running....'

    data_queue = Queue.Queue()

    data_server = dataServer('127.0.0.1', 1234, 10)
    data_server.daemon = True
    data_server.start()

    data_traveler = dataTraveler(data_queue, data_server.client_list)
    data_traveler.daemon = True
    data_traveler.start()

    data_producer = dataProducer(data_queue)
    data_producer.daemon = True
    data_producer.start()

    time.sleep(1)
    data_queue.join()
