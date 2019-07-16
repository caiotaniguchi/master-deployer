import json
import uuid
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError


class Producer:
    def __init__(self):
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=['kafka:9092'],
                key_serializer=lambda s: s.encode('ascii'),
                value_serializer=lambda m: json.dumps(m).encode('ascii')
            )
        except:
            time.sleep(1)
            self.__init__()


    def send(self, topic, key, value):
        self.producer.send(topic, key=key, value=value)\
                     .add_callback(self._on_send_success)\
                     .add_errback(self._on_send_error)
        self.producer.flush()


    @staticmethod
    def generate_key():
        return uuid.uuid4().hex


    @staticmethod
    def _on_send_success(record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)


    @staticmethod
    def _on_send_error(excp):
        print(excp)
        log.error('I am an errback', exc_info=excp)


    @staticmethod
    def _on_send_error(excp):
        print(excp)
        log.error('I am an errback', exc_info=excp)
