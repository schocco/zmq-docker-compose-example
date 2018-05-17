# ZMQ with docker-compose

docker-compose file with a simple ZMQ queue, based on the example presented on
http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/devices/queue.html


Start with:
```
docker-compose up --scale server=2 --scale client=4 
```
