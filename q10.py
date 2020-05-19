import pandas as pd
diamonds=pd.read_csv('C:/Users/dell/Downloads/diamonds.csv')
print("no of rows and columns:")
print(diamonds.shape)
print("after droping those rows where values are missing:")
print(diamonds.dropna(how='any').shape)