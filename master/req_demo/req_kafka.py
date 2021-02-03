from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
import sys
sys.path.insert(1, '/home/ubuntu/demo/master/')
from protobuf.data.request_pb2 import apidata

producer = KafkaProducer(bootstrap_servers=['10.100.240.4:30191'])

with open("input.json", "r") as f_input:
    json_input = json.load(f_input)

    for row in json_input:
        requestId = json_input.get('requestId')
        corporation_site_id = json_input.get('corporation_site_id')
        analysis_timeframe_start = json_input.get('analysis_timeframe_start')
        analysis_timeframe_end = json_input.get('analysis_timeframe_end')
        analysis_time_period = json_input.get('analysis_time_period')
        reqdata = apidata (
            request_id = requestId,
            corporation_site_id = corporation_site_id,
            analysis_timeframe_start = analysis_timeframe_start,
            analysis_timeframe_end = analysis_timeframe_end,
            analysis_time_period = analysis_time_period
            )
        producer.send('demo', value=reqdata.SerializeToString())
    producer.flush()


''' Response
with open("input.json", "r") as f_input:
    json_input = json.load(f_input)

    for row in json_input:
        requestId = json_input.get('requestId')
        resultCode = json_input.get('resultCode')
        resultPaths = json_input.get('resultPaths')
        reqdata = responsedata (
            requestId = requestId,
            resultCode = resultCode,
            resultPaths = resultPaths)
        producer.send('demo', value=reqdata.SerializeToString())
    producer.flush()
'''
