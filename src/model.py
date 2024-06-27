import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense 

def create_model(vocab_size, embedding_dim, hidden_dim, num_layers):
    """
    Creates and returns a text generation model
    """
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim))

    for _ in range(num_layers):
        model.add(LSTM(hidden_dim, return_sequences=True))


    model.add(Dense(vocab_size, activation='softmax'))
    return model