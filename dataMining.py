
import pandas as pd
from sklearn import metrics

import preProcessor
import model01
import model02
import model03
import model04


dfTrain = preProcessor.preProcessTrain("dataset_treino.csv")


dfTrain.to_csv("train-pre01.csv")

# Regressão Linear
x = ["Year Built", "Number of Buildings - Self-reported", "Occupancy", "Site EUI (kBtu/ft²)", "Largest Property Use Type (ft²)"]
y = "ENERGY STAR Score"
print(">>> Model01 - Linear Regression")
dfPrModel01 = model01.trainTest(dfTrain, x, y)
print('MAE Model 01:', metrics.mean_absolute_error(dfPrModel01['Test'],dfPrModel01['Prediction']))


##### Regressão Polinomial 
x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)", "GHG Emissions Area (Metric Tons CO2e/ft²)",
    "Year Built", "Number of Buildings - Self-reported", "Occupancy", "Code Property Type"]
y = "ENERGY STAR Score"
print(">>> Model02 - Poly Regression")
dfPrModel02 = model02.trainTest(dfTrain, x, y)
print('MAE Model 02:', metrics.mean_absolute_error(dfPrModel02['Test'],dfPrModel02['Prediction']))


### Rede Neural
x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)",
    "GHG Emissions Area (Metric Tons CO2e/ft²)", "Number of Buildings - Self-reported", "Code Property Type"]
x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)", "GHG Emissions Area (Metric Tons CO2e/ft²)",
    "Year Built", "Number of Buildings - Self-reported", "Occupancy", "Code Property Type"]
y = ["ENERGY STAR Score"]
print(">>> Model03 - Perceptron")
dfPrModel03 = model03.trainTest(dfTrain, x, y, 8)
print('MAE Model 03:', metrics.mean_absolute_error(dfPrModel03['Test'],dfPrModel03['Prediction']))



##### Gradient
x = ["Site EUI (kBtu/ft²)", "Site Gas (kBtu/ft²)", "Electricity Use Area (kBtu/ft²)", "GHG Emissions Area (Metric Tons CO2e/ft²)",
    "Year Built", "Number of Buildings - Self-reported", "Occupancy", "Code Property Type"]
y = "ENERGY STAR Score"
print(">>> Model04 - Gradient Boosting Regressor")
dfPrModel04 = model04.trainTest(dfTrain, x, y)
print('MAE Model 04:', metrics.mean_absolute_error(dfPrModel04['Test'],dfPrModel04['Prediction']))