import zmq
import random
import logging
import sys
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

address = os.environ["ZMQ_ADDRESS"]
context = zmq.Context()

logging.info("Connecting to server...")
socket = context.socket(zmq.REQ)
socket.connect(address)
client_id = random.randrange(1, 10005)

for request in range(1, 1000):
    logging.info("Sending request {}".format(request))
    socket.send_string("PING {} from client {}".format(request, client_id))
    #  Get the reply
    message = socket.recv()
    logging.info("Received reply {}: '{}'".format(request, str(message)))
