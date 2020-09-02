import pandas as pd


df = pd.read_csv("F:/out.csv")
#df.head()
#print(df)
df1=df.dropna()

df1.to_csv('F:/clo.csv', encoding='utf-8')

