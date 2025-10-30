import pandas as pd

#list generated using gemini
allcountries= ['AFGHANISTAN', 'ALBANIA', 'ALGERIA', 'ANDORRA', 'ANGOLA', 'ANTIGUA AND BARBUDA', 
    'ARGENTINA', 'ARMENIA', 'AUSTRALIA', 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 
    'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BHUTAN', 
    'BOLIVIA', 'BOSNIA AND HERZEGOVINA', 'BOTSWANA', 'BRAZIL', 'BRUNEI', 'BULGARIA', 
    'BURKINA FASO', 'BURUNDI', 'CABO VERDE', 'CAMBODIA', 'CAMEROON', 'CANADA', 
    'CENTRAL AFRICAN REPUBLIC', 'CHAD', 'CHILE', 'CHINA', 'COLOMBIA', 'COMOROS', 
    'CONGO (CONGO-BRAZZAVILLE)', 'COSTA RICA', 'COTE D\'IVOIRE', 'CROATIA', 'CUBA', 
    'CYPRUS', 'CZECHIA (CZECH REPUBLIC)', 'DEMOCRATIC REPUBLIC OF THE CONGO', 
    'DENMARK', 'DJIBOUTI', 'DOMINICA', 'DOMINICAN REPUBLIC', 'ECUADOR', 'EGYPT', 
    'EL SALVADOR', 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ESWATINI (FKA SWAZILAND)', 
    'ETHIOPIA', 'FIJI', 'FINLAND', 'FRANCE', 'GABON', 'GAMBIA', 'GEORGIA', 'GERMANY', 
    'GHANA', 'GREECE', 'GRENADA', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 
    'HAITI', 'HONDURAS', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 
    'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 
    'KIRIBATI', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 
    'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 
    'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MAURITANIA', 'MAURITIUS', 'MEXICO', 
    'MICRONESIA', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MOROCCO', 'MOZAMBIQUE', 
    'MYANMAR (FKA BURMA)', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NEW ZEALAND', 
    'NICARAGUA', 'NIGER', 'NIGERIA', 'NORTH KOREA', 'NORTH MACEDONIA', 'NORWAY', 'OMAN', 
    'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES', 
    'POLAND', 'PORTUGAL', 'QATAR', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT KITTS AND NEVIS', 
    'SAINT LUCIA', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 
    'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA', 'SEYCHELLES', 
    'SIERRA LEONE', 'SINGAPORE', 'SLOVAKIA', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 
    'SOUTH AFRICA', 'SOUTH KOREA', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA', 'SUDAN', 
    'SURINAME', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 
    'TIMOR-LESTE', 'TOGO', 'TONGA', 'TRINIDAD AND TOBAGO', 'TUNISIA', 'TURKEY', 
    'TURKMENISTAN', 'TUVALU', 'UGANDA', 'UKRAINE', 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 
    'UNITED STATES OF AMERICA', 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 
    'YEMEN', 'ZAMBIA', 'ZIMBABWE'
]

print("start of inflation!!!!!!!")
print('Read in inflation')
df = pd.read_csv('inflation.csv')


print("REMOVE THE UNWANTED COLUMNS")
df_new = df.drop(["Inflation, GDP deflator (annual %)", "Deposit interes (%)" ,"Unemployment, total (% of total labor force) (national estimate)", "iso3c","iso2c","adminregion"], axis=1)
print(df_new.columns) #NICE

#fill in NaN values
df_new = df_new.fillna(0)


#change data types
df_new['country'] = df_new['country'].astype(str)#change to string datatype
df_new['year'] = df_new['year'].astype(int)
df_new['Inflation, consumer prices (ant rate (%),Lending interest ratenual %)'] = df_new['Inflation, consumer prices (ant rate (%),Lending interest ratenual %)'].astype(float)
df_new['Real interest rate (%)'] = df_new['Real interest rate (%)'].astype(float)
df_new['Unemployment, total (% of total labor force) (modeled ILO estimate)'] = df_new['Unemployment, total (% of total labor force) (modeled ILO estimate)'].astype(float)
df_new['incomeLevel'] = df_new['incomeLevel'].astype(str)#change to string datatype


df_new['country'] = df_new['country'].str.upper() # make the country column uppercase
df_new['country'] = df_new['country'].str.replace('"', '') #remove quotes in the column (helps with bahamas)
df_new = df_new[df_new['country'].isin(allcountries)] #see if the instances of country exists in a list of all countries today

print(df_new)


#remove spaces
df_new.columns = df_new.columns.str.strip() #delete whitespace

#remove rows
#is_in_list = df_new['country'].isin(allcountries) #see if the instances of country exists in a list of all countries today
df_new = df_new[(df_new['year'] >= 1970) & (df_new['year'] <= 2021)] #only instances from 1970-2021
print(df_new)

print(df_new.head())
print(df_new.info())
print(df_new.describe())
print(df_new.isnull().sum())
print(df_new.isnull().any())



print("start of olympics!!!!!!!")
print('read in olympics')
df1 = pd.read_csv('olympics.csv')

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
df1 = df1[(df1['Year'] >= 1970) & (df1['Year'] <= 2021)]


print("start of GDP!!!!!!!")
print('read in GDP')
df2 = pd.read_csv('gdp.csv', sep=';')

print(df2.head())
print(df2.info())
print(df2.describe())
print(df2.isnull().sum())
print(df2.isnull().any())

#remove spaces
df2.columns = df2.columns.str.strip()

#fill in NaN values
df2 = df2.fillna(0)

#Years and columns we want
year_cols = [col for col in df2.columns if col.isdigit() and int(col) <= 2021]
df2 = df2[['country_name', 'indicator_name'] + year_cols] 

# confirm data type in each column and what we did to make sure it was correct
