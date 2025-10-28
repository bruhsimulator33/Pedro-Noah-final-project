import pandas as pd
import numpy as np

inflation = pd.read_csv("inflation.csv")
olympics = pd.read_csv("olympics.csv")
gdp = pd.read_csv("gdp.csv",encoding='latin1')


print(inflation.head())
print(olympics.head())
print(gdp.head())

filtered_inflation = inflation[inflation['year'] <= 2021]

##### range from 1980-2021 
# gdp is from 1980-2024
# inflation from 1970-2021
#olympics from 1890-2024

