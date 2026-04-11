import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("../data/sales.csv")

df["MonthNo"] = np.arange(len(df))

X = df[["MonthNo"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X,y)

future = [[12]]
prediction = model.predict(future)

print("Next Month Sales Prediction:", int(prediction[0]))
