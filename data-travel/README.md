data-travel
===========
version: 0.0.1

**HOW TO USE**

    ```
    from dataTraveler import dataTraveler
    from dataServer import dataServer
    from dataProducer import dataProducer
    
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
    ```

**Author**

Tony Su
