#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/ubuntu/demo/master/')


from MessageCorps.broker import kafka_consumer
import logging

logging.basicConfig(level=logging.ERROR)


def main():
    consumer = kafka_consumer(bootstrap_servers="10.100.240.4:30191", topic="demo")

    for message in consumer.consume():
        print(message)


if __name__ == '__main__':
    main()
