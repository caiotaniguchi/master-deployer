from abc import ABC, abstractmethod
import os

import joblib


class LearningModel(ABC):
    def __init__(self, learning_model_file):
        if os.path.isfile(learning_model_file):
            self.clf = joblib.load(learning_model_file)
        self.learning_model_file = learning_model_file
        super().__init__()

    @abstractmethod
    def fit(self, training_data):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass
