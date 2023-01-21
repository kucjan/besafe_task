from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np


class LoadedModel(object):
    def __init__(self, model_path, test_images, test_results, custom_objects=None):
        if custom_objects is None:
            self.model = keras.models.load_model(model_path)
        else:
            self.model = keras.models.load_model(
                model_path, custom_objects=custom_objects
            )
        self.test_images = test_images
        self.test_results = test_results
        self.predictions = self.model.predict(self.test_images)

    def rounded_acc(self, predict_threshold):
        correct_count = 0
        for prediction, result in zip(self.predictions, self.test_results):
            if all((abs(prediction - result)) < predict_threshold):
                correct_count += 1

        return correct_count / self.predictions.shape[0]

    def draw_prediction(self, id):
        plt.gray()
        plt.imshow(self.test_images[id])
        plt.scatter(
            x=[self.predictions[id][1], self.predictions[id][3]],
            y=[self.predictions[id][0], self.predictions[id][2]],
            c="r",
            s=20,
        )
        plt.suptitle(
            "Start: {}, end: {}".format(
                (self.test_results[id][0], self.test_results[id][1]),
                (self.test_results[id][2], self.test_results[id][3]),
            )
        )
        plt.title(
            "Pred. start: {}, pred. end: {}".format(
                (self.predictions[id][0], self.predictions[id][1]),
                (self.predictions[id][2], self.predictions[id][3]),
            )
        )
        plt.show()
