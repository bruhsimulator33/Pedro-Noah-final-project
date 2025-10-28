import pandas as pd


print('Read in inflation')
df = pd.read_csv('inflation_interest_unemployment.csv')

#remove spaces
df.columns = df.columns.str.strip()

#remove rows
df = df[(df['year'] >= 1980) & (df['year'] <= 2021)]

#fill in NaN values
df = df.fillna(0)


print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.isnull().any())


print('read in olympics')
df1 = pd.read_csv('olympics_dataset.csv')

print(df1.head())
print(df1.info())
print(df1.describe())
print(df1.isnull().sum())
print(df1.isnull().any())
#remove spaces
df1.columns = df1.columns.str.strip()

#fill in NaN values
df1 = df1.fillna(0)

#remove rows
df1 = df1[(df1['Year'] >= 1980) & (df1['Year'] <= 2021)]

print('read in GDP')
df2 = pd.read_csv('world_gdp_data.csv', encoding='latin1')

print(df2.head())
print(df2.info())
print(df2.describe())
print(df2.isnull().sum())
print(df2.isnull().any())

#remove spaces
df.columns = df.columns.str.strip()

#fill in NaN values
df2 = df2.fillna(0)

#Years and columns we want
year_cols = [col for col in df2.columns if col.isdigit() and int(col) <= 2021]
df2 = df2[['country_name', 'indicator_name'] + year_cols] 

