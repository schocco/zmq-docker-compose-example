import random
import time
import logging
import sys
import os

import zmq

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

address = os.environ["ZMQ_ADDRESS"]
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect(address)
server_id = random.randrange(1, 10005)
logging.info("Starting server {}".format(server_id))
while True:
    #  Wait for next request from client
    message = socket.recv()
    logging.info("Received request: {}".format(message))
    time.sleep(1)
    socket.send_string("PONG from server {}".format(server_id))
