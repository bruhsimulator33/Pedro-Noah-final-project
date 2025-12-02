import pandas as pd
import numpy as np

# echo "# Pedro-Noah-final-project" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:bruhsimulator33/Pedro-Noah-final-project.git
# git push -u origin main

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

