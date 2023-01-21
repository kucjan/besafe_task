# Line Detector

This project aims to train a neural network to recognize the coordinates of the start and end of a line in an image. The image is represented as a 2D array full of ones and the line is represented by connected zeros in the array.

## Project Structure

The project is organized as follows:

- `src` directory contains all the scripts for the project, including:
  - `LineDatasetGenerator.py` - class for generating dataset of images with lines
  - `train_model.ipynb` - notebook for training the model
  - `LoadedModel.py` - class for loading and using previously saved model
  - `test_model.ipynb` - notebook for testing the model on new data
- `models` directory contains saved models

## Results

Choosing th final version of model was decision between highly overfitting network with satisfying results on training data or model in which overfitting was eliminated by dropouts and regularizers, at the sacrifice of acceptable precision - training and validation loss (MSE) were on about 140 level. Version with overfitting and good results on training set was left to show that the prediction works fine at least there.

## Installation

1. Make sure you have python3 installed in your system. 
2. Clone the repository:
```bash
$ git clone https://github.com/kucjan/besafe_task.git
```
2. Navigate to the project directory.
3. Create and activate a virtual environment:
```bash
$ python3 -m venv besafe_taskenv
$ source besafe_taskenv/bin/activate
```
4. Install the required packages:
```bash
$ pip3 install -r requirements.txt
```
5. Open the `train_model.ipynb` notebook to see how model was built and what are the results.
  You can run last cell to test saved model on training data.
6. Run the `test_model.ipynb` notebook to test saved model on new data.
7. Once you're done working on the project, deactivate the virtual environment:
```bash
$ deactivate
```