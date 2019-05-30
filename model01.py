# encoding: utf-8

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def resultToInt(x):
    xint = int(x)

    if xint > 100:
        xint = 100
    if xint < 0:
        xint = 0

    return xint

def trainTest(dftt, x, y):
    # dftt - DF Train and Test
    ## SPlit Dataset to train and test
    x_train, x_test, y_train, y_test = train_test_split(dftt[x], dftt[y], test_size=0.20, random_state=101)
    
    model = LinearRegression()
    
    model.fit(x_train, y_train)
    
    prediction = model.predict(x_test)
    
    
    result = pd.DataFrame(columns=['Test', 'Prediction'])
    result['Test'] = y_test
    result['Prediction'] = prediction
    result['Prediction'] = result['Prediction'].apply(resultToInt)
    return result
    
    
def trainPredict(dft, dfp, x, y):
    # dft - DF Train,
    # dfp - DF Pprediction
    model = LinearRegression()
    
    model.fit(dft[x], dft[y])
    
    prediction = model.predict(dfp[x])

    result = pd.DataFrame(columns=['Property Id', 'score'])
    result['Property Id'] = dfp['Property Id']
    result['score'] = prediction
    result['score'] = result['score'].apply(resultToInt)

    result.to_csv('submission.csv',index=False)
    
    return 'ok'

