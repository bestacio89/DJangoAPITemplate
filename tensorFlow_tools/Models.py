import tensorflow as tf
from tensorflow.keras import layers, models

def create_basic_model(input_shape, num_classes):
    """
    Creates a basic Convolutional Neural Network model.

    Args:
    - input_shape (tuple): Shape of the input data (e.g., (height, width, channels)).
    - num_classes (int): Number of output classes.

    Returns:
    - tf.keras.Model: Compiled Keras model.
    """
    model = models.Sequential([
        layers.InputLayer(input_shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def create_lstm_model(input_shape, num_classes):
    """
    Creates a basic LSTM model.

    Args:
    - input_shape (tuple): Shape of the input data (e.g., (sequence_length, input_dim)).
    - num_classes (int): Number of output classes.

    Returns:
    - tf.keras.Model: Compiled Keras model.
    """
    model = models.Sequential([
        layers.InputLayer(input_shape=input_shape),
        layers.LSTM(64),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model
