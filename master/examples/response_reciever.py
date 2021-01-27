#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/ubuntu/demo/master/')


from MessageCorps.broker2 import kafka_consumer
import logging

logging.basicConfig(level=logging.ERROR)


def main():
    consumer = kafka_consumer(bootstrap_servers="192.168.254.194:9094", topic="demo-output")

    for message in consumer.consume():
        print(message)


if __name__ == '__main__':
    main()