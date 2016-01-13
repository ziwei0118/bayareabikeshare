import pandas as pd

df1 = pd.read_csv('data/raw/201402_trip_data.csv')
df2 = pd.read_csv('data/raw/201408_trip_data.csv')
df3 = pd.read_csv('data/raw/201508_trip_data.csv')

df1.loc[:0,:]
df2.loc[:0,:]
df3.loc[:0,:]

df = pd.concat([df1, df2, df3], ignore_index=True)
#df = df1.append([df2, df3])

df1.shape
df2.shape
df3.shape
df.shape

df = df[df1.columns]

df['Start Date'] = pd.to_datetime(df['Start Date'])
#df['End Date'] = pd.to_datetime(df['End Date'])

df = df.sort_values('Start Date')
df.to_csv('data/trip_data.csv',index=False)
