import pandas as pd
diamonds=pd.read_csv('C:/Users/dell/Downloads/diamonds.csv')
print("original dataframe:")
print(diamonds.head())
print("count , min, max price for each cut of the above dataframe:")
print(diamonds.groupby('cut').price.agg(['count','min','max']))