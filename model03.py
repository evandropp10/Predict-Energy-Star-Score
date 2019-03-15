# encoding: utf-8

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing.text import one_hot
from sklearn.model_selection import train_test_split


def resultToInt(x):
    xint = int(x)

    if xint > 100:
        xint = 100
    if xint < 0:
        xint = 0

    return xint

def trainTest(dftt, x, y):
    print("3")
    # dftt - DF Train and Test
    ## SPlit Dataset to train and test
    
    x_train, x_test, y_train, y_test = train_test_split(dftt[x], dftt[y], test_size=0.20, random_state=101)
    
    x_arrTrain = np.array(x_train)
    x_arrTest = np.array(x_test)
    y_arrTrain = np.array(y_train)
    y_arrTest = np.array(y_test)

    # create model

    model = Sequential()
    model.add(Dense(12, input_dim=6, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='linear'))
    
    # Compile model
    model.compile(loss='mse', optimizer='adam')

    model.fit(x_arrTrain, y_arrTrain, epochs=150, verbose=0)

    prediction = model.predict(x_arrTest)

    result = pd.DataFrame(columns=['Test', 'Prediction'])
    result['Test'] = y_test
    result['Prediction'] = prediction
    result['Prediction'] = result['Prediction'].apply(resultToInt)
    return result
    
    
def trainPredict(dft, dfp, x, y):
    # dft - DF Train,
    # dfp - DF Pprediction
    x_arrTrain = np.array(dft[x])
    x_arrTest = np.array(dfp[x])
    y_arrTrain = np.array(dft[y])


    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=6, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='linear'))
    
    # Compile model
    model.compile(loss='mse', optimizer='adam')

    model.fit(x_arrTrain, y_arrTrain, epochs=150, verbose=0)

    prediction = model.predict(x_arrTest)

    result = pd.DataFrame(columns=['Property Id', 'score'])
    result['Property Id'] = dfp['Property Id']
    result['score'] = prediction
    result['score'] = result['score'].apply(resultToInt)
    
    return result




############# teste

from sklearn import metrics

import preProcessor
#import model01
#import model02
import model03


dfTrain = preProcessor.preProcessTrain("dataset_treino.csv")

x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)",
    "GHG Emissions Area (Metric Tons CO2e/ft²)", "Number of Buildings - Self-reported", "Code Property Type"]
y = "ENERGY STAR Score"
print(">>> Model31 - Perceptron")
dfPrModel02 = trainTest(dfTrain, x, y)
print('MAE Model 32:', metrics.mean_absolute_error(dfPrModel02['Test'],dfPrModel02['Prediction']))