from model.base_model import LearningModel
import joblib


class DumbModel(LearningModel):
    def fit(self, training_data):
        from sklearn import svm, datasets

        training_data = datasets.load_iris()
        X, y = training_data.data, training_data.target

        clf = svm.SVC(gamma='scale')
        clf.fit(X, y)
        joblib.dump(clf, self.learning_model_file)

    def predict(self, input_data):
        if self.clf is None:
            self.clf = joblib.load(self.learning_model_file)
        return self.clf.predict(input_data)
