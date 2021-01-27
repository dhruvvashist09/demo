#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/ubuntu/demo/master/')

from MessageCorps.broker import kafka_producer
from protobuf.data.request_schema_pb2 import apidata
from time import sleep
import logging

logging.basicConfig(level=logging.ERROR)

def main():

    producer = kafka_producer(bootstrap_servers=['10.100.240.4:30191'], topic="demo")

    reqdata = apidata(request_id = "60bd976a-5281-11eb-b79b-067d9753f7ac",corporation_id = 100,site_id = 10153, analysis_timeframe_start=1610215913,analysis_timeframe_end=1610216000,analysis_time_period =10)
    for frame in range(10):
       #reqdata.frame = frame
        producer.send(reqdata)
        sleep(1)



if __name__ == "__main__":
    main()
