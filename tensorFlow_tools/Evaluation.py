import tensorflow as tf

def evaluate_model(model, test_data, test_labels):
    results = model.evaluate(test_data, test_labels, verbose=2)
    return results
