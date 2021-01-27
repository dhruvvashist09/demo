#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/ubuntu/demo/master/')

from MessageCorps.broker import kafka_producer
from protobuf.data.response_schema_pb2 import apidata
from time import sleep
import logging

logging.basicConfig(level=logging.ERROR)

def main():

    producer = kafka_producer(bootstrap_servers=['192.168.254.194:9094'], topic="demo-output")

    reqdata = apidata(requestId = b"60bd976a-5281-11eb-b79b-067d9753f7ac",resultCode = "Complete",resultPaths = [{"type":"orc","path":"demo/c1df5357-fc9d-4a8a-b806-12517c60f17e/"},{"type":"csv","path":"demo/c1df5357-fc9d-4a8a-b806-12517c60f17e/"}])
    for frame in range(10):
       #reqdata.frame = frame
        producer.send(reqdata)
        sleep(1)



if __name__ == "__main__":
    main()