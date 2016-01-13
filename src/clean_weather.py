import pandas as pd

df1 = pd.read_csv('data/201402_weather_data.csv')
df2 = pd.read_csv('data/201408_weather_data.csv')
df3 = pd.read_csv('data/201508_weather_data.csv')

df1.columns.tolist()  == df3.columns.tolist()

df2.columns = df1.columns
df3.columns = df1.columns

df = pd.concat([df1, df2, df3], ignore_index=True)

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['Date', 'zip'])

df.loc[:,:].isnull().any()
