import threading
import Queue
import time


class dataProducer(threading.Thread):

    def __init__(self, data_queue):
        super(dataProducer, self).__init__()
        self.data_queue = data_queue

    def run(self):
        data = 1
        while True:
            self.data_queue.put(str(data))
            data += 1
            time.sleep(1)


if __name__ == "__main__":
    data_queue = Queue.Queue()
    data_producer = dataProducer(data_queue)
    data_producer.daemon = True
    data_producer.start()
    while True:
        data = data_queue.get()
        print data
