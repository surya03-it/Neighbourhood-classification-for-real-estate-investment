# -*- coding: utf-8 -*-
"""Real Estate.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1axxwe9rkafrI-RYVwCtM_WNhBOYAPApV
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df=pd.read_csv("/content/data.csv")

df

df.info()

df.describe()

df['RM']=df['RM'].fillna(df['RM'].mean())

df.info()

print("Total Number of Missing Value",df.isna().sum())

y=df['MEDV'].copy()
x=df.drop('MEDV',axis=1)

x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

scaler=StandardScaler()
scaler.fit(x_train)
x_train=pd.DataFrame(scaler.transform(x_train),columns=x_train.columns)
x_test=pd.DataFrame(scaler.transform(x_test),columns=x_test.columns)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

model=RandomForestRegressor()
model.fit(x_train,y_train)
print(model.score(x_test,y_test))

