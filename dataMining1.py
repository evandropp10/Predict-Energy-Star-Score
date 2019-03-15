
import pandas as pd
from sklearn import metrics

import preProcessor
import model03 # PErceptron Keras


dfTrain = preProcessor.preProcessTrain("dataset_treino.csv")

### TESTANDO O MODELO
x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)",
    "GHG Emissions Area (Metric Tons CO2e/ft²)", "Number of Buildings - Self-reported", "Code Property Type"]
y = "ENERGY STAR Score"
print(">>> Model31 - Perceptron")
dfPrModel = model03.trainTest(dfTrain, x, y)
print('MAE Model 32:', metrics.mean_absolute_error(dfPrModel['Test'],dfPrModel['Prediction']))


### REALIZANDO A PREDICAO
dfTest = preProcessor.preProcessTrain("dataset_teste.csv")

dfPrModel = model03.trainPredict(dfTrain, dfTest, x, y)

dfPrModel.to_csv("submission.csv", index=False)
