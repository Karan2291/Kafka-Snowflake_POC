from kafka import KafkaConsumer
import json
consumer = KafkaConsumer('user_topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='latest',
                         group_id="consumer_group_a")
print("Starting Consumer")
for message in consumer:
    print("User-data: {}".format(json.loads(message.value)))