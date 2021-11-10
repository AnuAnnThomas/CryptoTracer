from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import LSTM


def lstm_model(x, y):
    regressor = Sequential()
    regressor.add(LSTM(units = 50, activation = 'sigmoid', return_sequences=True, input_shape = (None, 1)))
    regressor.add(Dropout(0.28))
    regressor.add(LSTM(units=50, activation='sigmoid'))
    regressor.add(Dropout(0.28))
    regressor.add(Dense(units = 1))
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    regressor.fit(x, y, batch_size = 15, epochs = 100)
    return regressor
