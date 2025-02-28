import pandas as pd
df = pd.read_csv(r"E:\PROYECTOS DATA ENGINEER\movies\movies.csv")
#print(df.head())
#print(df.tail())
print(df.columns)
#ordenado = df[(df['release_date']>='2010-01-01')]
#print(df['title'])
print(df[(df['release_date']>='2010-01-01')])
