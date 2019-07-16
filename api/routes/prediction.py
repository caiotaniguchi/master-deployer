import json

import falcon

from utils.producer import Producer


class Predictor:
    def __init__(self):
        self.producer = Producer()

    def on_post(self, req, resp, model_name):
        key = self.producer.generate_key()
        self.producer.send(model_name, key, json.load(req.bounded_stream))
        resp.body = json.dumps({'job_id': key}, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_get(self, req, resp, model_name):
        pass
