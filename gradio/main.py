import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import gradio as gr

from gru import gru_model
from lstm import lstm_model
from rnn import rnn_model

PREDICT_DAYS = 50

def read_file_and_predict(choice,file):
    sc = MinMaxScaler()
    df = pd.read_csv(file.name)
    df=df[['Date', 'Closing Price (USD)']]
    df.columns = ['Date', 'Price']
    df_train = df.Price[:len(df.Price)-PREDICT_DAYS]
    df_test = df.Price[len(df.Price)-PREDICT_DAYS:]
    training_set = df_train.values
    training_set = np.reshape(training_set, (len(training_set), 1))
    training_set = sc.fit_transform(training_set)
    X_train = training_set[0:len(training_set)-1]
    X_train = np.reshape(X_train, (len(X_train), 1, 1))
    Y_train = training_set[1:len(training_set)]

    if(choice=="LSTM"):
        model = lstm_model(X_train, Y_train)
    elif(choice =="GRU"):
        model = gru_model(X_train, Y_train)
    elif(choice=="RNN"):
        model = rnn_model(X_train, Y_train)

    test_set = df_test.values
    inputs = np.reshape(test_set, (len(test_set), 1))
    inputs = sc.transform(inputs)
    inputs = np.reshape(inputs, (len(inputs), 1, 1))
    predicted_prices = model.predict(inputs)
    predicted_prices = sc.inverse_transform(predicted_prices)
    plt.figure(figsize=(60, 32), dpi=300, facecolor='w', edgecolor='k')
    ax = plt.gca()
    plt.plot(test_set, color='red', label='Real Price')
    plt.plot(predicted_prices, color='blue', label='Predicted Price')
    # plt.title('Using LSTM', fontsize=40)
    df_test = df_test.reset_index()
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(10)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(10)
    plt.xlabel('DATE', fontsize=20)
    plt.ylabel('Price (USD)', fontsize=20)
    plt.legend(loc=2, prop={'size': 16})
    return plt.gcf()


iface = gr.Interface(read_file_and_predict,
                    [gr.inputs.Dropdown(["LSTM", "GRU", "RNN"]), gr.inputs.File()],
                     outputs=["plot"],
                     description="Cryptocurrency Prediction"
                     )
iface.launch()
