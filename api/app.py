import falcon

from routes.prediction import Predictor


api = application = falcon.API()

api.add_route('/prediction/{model_name}', Predictor())
