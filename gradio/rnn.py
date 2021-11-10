from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import SimpleRNN

def rnn_model(x, y):
    regr = Sequential() 
    regr.add(SimpleRNN(units =50, activation ='relu', return_sequences=True, input_shape =(None, 1)))    
    regr.add(Dropout(0.4))
    regr.add(SimpleRNN(units=50))
    regr.add(Dropout(0.4))
    regr.add(Dense(units =1))
    regr.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy']) 
    regr.fit(x,y, batch_size =5, epochs =150)  
    return regr