from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import GRU

def gru_model(x, y):
    regressor = Sequential()
    regressor.add(GRU(units = 20, activation = 'tanh',return_sequences=True, input_shape = (None, 1)))
    regressor.add(Dropout(0.28))
    regressor.add(GRU(units = 20, activation = 'tanh',return_sequences=True))
    regressor.add(Dropout(0.28))
    regressor.add(GRU(units = 20, activation = 'tanh'))
    regressor.add(Dropout(0.28))
    regressor.add(Dense(units = 1))
    regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    regressor.fit(x, y, batch_size = 15, epochs = 100)
    return regressor



