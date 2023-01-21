from random import choice
import numpy as np
import sys
from dataset_generator import DatasetGenerator

np.set_printoptions(threshold=sys.maxsize)

my_range = range(-4, 4)

for i in my_range:
    print(i)
    print("random: {}".format(choice(my_range)))


array = np.zeros((64, 64))

point = (3, 2)

print(array[point])

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "stop": (0, 0),
}
move = choice(list(possible_moves.keys()))

print(move)

tr = DatasetGenerator((64, 64))

arr, start, end = tr.generate_image()

print(arr)

print(arr.flatten())

print(len(arr.flatten()))
print(type(arr.flatten()))

train_images, train_results = tr.create_set(100)

print(train_images.shape)
print(train_results.shape)

tr.draw_image(train_images[4])
