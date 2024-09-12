# generalutilities/DataHandler.py
import numpy as np

def normalize_data(data):
    """Normalizes data to have zero mean and unit variance."""
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean) / std

def one_hot_encode(labels, num_classes):
    """One-hot encodes a list of labels."""
    return np.eye(num_classes)[labels]
