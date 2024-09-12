import tensorflow as tf

def train_model(model, train_data, train_labels, validation_data=None, epochs=10, batch_size=32):
    history = model.fit(
        train_data,
        train_labels,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=validation_data
    )
    return history
