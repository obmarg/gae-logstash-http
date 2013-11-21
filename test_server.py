import zmq

if __name__ == '__main__':
    context = zmq.Context.instance()
    socket = context.socket(zmq.PULL)
    socket.bind('tcp://*:2120')

    while True:
        x = socket.recv()
        print x
