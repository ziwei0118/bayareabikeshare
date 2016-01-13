import pandas as pd

df1 = pd.read_csv('data/raw/201402_status_data.csv')
df2 = pd.read_csv('data/raw/201408_status_data.csv')
df3 = pd.read_csv('data/raw/201508_status_data.csv')

df1.isnull().any()
df2.isnull().any()
df3.isnull().any()

df1.station_id.value_counts()
df = pd.concat([df1, df2, df3],ignore_index=True)

del df1, df2, df3

df.to_csv('data/status_data.csv',index=False)
