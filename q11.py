import pandas as pd
diamonds=pd.read_csv('C:/Users/dell/Downloads/diamonds.csv')
print("original dataset:")
print(diamonds.shape)
print("duplicate rows:")
print(diamonds.duplicated().sum())