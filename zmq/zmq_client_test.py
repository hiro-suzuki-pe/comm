import zmq
import time

host = '127.0.0.1'
port = 5555
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))
for num in range(1, 10):
    time.sleep(0.3)
    request_str = "message #%s_copy #" % num
    request_bytes = request_str.encode('utf-8')
    client.send(request_bytes)
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print("Sent %s, received %s_copy #" % (request_str, reply_str))