# Gender Classification Model for Indian Faces

This project implements a deep learning model for gender classification, specifically trained on Indian faces. The model uses TensorFlow and Keras to predict whether a given image contains a male or female face.

## Features

- Trained on a dataset of Indian faces for improved accuracy in this demographic
- Uses a Convolutional Neural Network (CNN) architecture
- Achieves high accuracy in gender prediction
- Provides confidence scores for predictions

## Requirements

- Python 3.11
- TensorFlow 
- NumPy
- Matplotlib
- Keras

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/gender-classification-indian-faces.git
   ```
2. Install the required packages:
   ```
   pip install tensorflow numpy matplotlib
   ```

## Usage

1. Ensure you have the trained model file `Gender_Classification_Model_by_Pratz.h5` in your project directory.

2. Use the attached python code to predict the gender of a new image:

  
## Model Details

The model is a Convolutional Neural Network (CNN) trained on a dataset of Indian faces. It takes an input image of size 150x150 pixels and outputs a binary classification (Male/Female) with a confidence score.

## Limitations

- The model is specifically trained on Indian faces and may not perform at the same level on faces from other ethnicities.
- As with all machine learning models, there may be biases present in the training data that could affect the model's predictions.

## Contributing

Contributions to improve the model or extend its functionality are welcome. Please feel free to submit pull requests or open issues to discuss potential changes.
Also help regarding giving bigger datasets including even more range of faces would be helpful.
Thank You
