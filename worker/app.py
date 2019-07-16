import time
import json

from kafka import KafkaConsumer

from model.dumb_model import DumbModel


def start_consumer(topic):
    try:
        return KafkaConsumer(
            topic,
            group_id='my-group',
            bootstrap_servers=['kafka:9092'],
            key_deserializer=lambda s: s.decode('ascii'),
            value_deserializer=lambda m: json.loads(m.decode('ascii'))
        )
    except:
        time.sleep(1)
        return start_consumer(topic)

consumer = start_consumer('dumb_model')

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
