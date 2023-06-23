from kafka import KafkaProducer
import json
from data import get_data
import time

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = json_serializer)

if __name__ == '__main__':
    while True:
        user_data = get_data()
        print(user_data)
        producer.send("user_topic",user_data) 
        time.sleep(2)

