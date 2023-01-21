import numpy as np
from random import randint, choices
import matplotlib.pyplot as plt


class LineDatasetGenerator(object):
    def __init__(self, image_size):
        self.image_size = image_size

    def generate_image(self):
        image = np.ones(self.image_size, dtype=int)
        image_height = self.image_size[0]
        image_width = self.image_size[1]

        start = (randint(0, image_height - 1), randint(0, image_width - 1))
        end = (randint(0, image_height - 1), randint(0, image_width - 1))

        if start == end:
            image[start] = 0
            return image, start, end
        elif start[0] == end[0]:
            for y in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                image[start[0]][y] = 0
        elif start[1] == end[1]:
            for x in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                image[x][start[1]] = 0
        else:
            num_of_steps = max(abs(start[0] - end[0]), abs(start[1] - end[1])) + 1
            x_axis_steps = np.linspace(start[0], end[0], num_of_steps, dtype=int)
            y_axis_steps = np.linspace(start[1], end[1], num_of_steps, dtype=int)
            for x, y in zip(x_axis_steps, y_axis_steps):
                image[x][y] = 0
        return image, start, end

    def create_set(self, set_size):
        images = np.zeros((set_size, self.image_size[0], self.image_size[1]), dtype=int)
        results = np.zeros((set_size, 4), dtype=int)
        for i in range(set_size):
            image, start, end = self.generate_image()
            images[i] = image
            results[i] = np.array([start[0], start[1], end[0], end[1]])
        return images, results

    def draw_random_image(self):
        plt.gray()
        image, start, end = self.generate_image()
        plt.imshow(image)
        plt.title(
            "Start point: {}, end point: {}".format(
                (start[0], start[1]), (end[0], end[1])
            )
        )
        plt.show()

    def draw_image(self, image, result=None):
        plt.gray()
        plt.imshow(image)
        if result is not None:
            plt.title(
                "Start point: {}, end point: {}".format(
                    (result[0], result[1]), (result[2], result[3])
                )
            )
        plt.show()
