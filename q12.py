import pandas as pd
diamonds=pd.read_csv("C:/Users/dell/Downloads/diamonds.csv")
print("original dataset")
print(diamonds.shape)
print("sample 75% of diamonds dataset's rows ithout replacemnt")
r=diamonds.sample(frac=0.75,random_state=99)
print(r)
print("remaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(r.index), :])