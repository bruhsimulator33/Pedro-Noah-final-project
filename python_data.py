import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


conn = mysql.connector.connect(
    host='db.cs.usna.edu',
    user='m270978',
    password='m270978',
    database='m270978'
)
# LIST OF HOST COUNTRIES WE WILL SHOW TO AVOID THE MOST MAJOR ECONOMIC EVENTS (FALL OF THE SOVIET UNION STILL PROBABLY HURT THE DATA)
# UNITED STATES,1984,Los Angeles
# SOUTH KOREA,1988,Seoul
# SPAIN,1992,Barcelona

##### START WITH UNITED STATES
gdp_query = """
SELECT g.Country, g.year, g.total_gdp_million
FROM gdp g
JOIN olympics o ON g.Country = o.Country
WHERE g.year BETWEEN 1984 - 4 AND 1984 + 4
AND g.Country IN ('UNITED STATES')
""" #4 years before host countries gdp

gdp_df = pd.read_sql(gdp_query, conn)

# Plot GDP over 4 years for all host countries
plt.figure(figsize=(10,6))
unitedstates_df = gdp_df[gdp_df['Country'] == 'UNITED STATES']
plt.plot(
    unitedstates_df['year'],
    unitedstates_df['total_gdp_million'],
    marker='o',
    color='green',
    label='UNITED STATES'
)

plt.xlabel('Year')
plt.ylabel('Total GDP (Million)')
plt.title('GDP of the United States: 4 Years before and after the 1984 Olympics')
plt.legend()
plt.tight_layout()
plt.savefig('gdp_unitedstates.png')


##### ON to SOUTH KOREA
gdp_query = """
SELECT g.Country, g.year, g.total_gdp_million
FROM gdp g
JOIN olympics o ON g.Country = o.Country
WHERE g.year BETWEEN 1988 - 4 AND 1988 + 4
AND g.Country IN ('SOUTH KOREA')
""" #4 years before host countries gdp

gdp_df = pd.read_sql(gdp_query, conn)

# Plot GDP over 4 years for all host countries
plt.figure(figsize=(10,6))
southkorea_df = gdp_df[gdp_df['Country'] == 'SOUTH KOREA']
plt.plot(
    southkorea_df['year'],
    southkorea_df['total_gdp_million'],
    marker='o',
    color='red',
    label='SOUTH KOREA'
)

plt.xlabel('Year')
plt.ylabel('Total GDP (Million)')
plt.title('GDP of South Korea: 4 Years before and after the 1988 Olympics')
plt.legend()
plt.tight_layout()
plt.savefig('gdp_southkorea.png')

####### Finally onto SPAIN
gdp_query = """
SELECT g.Country, g.year, g.total_gdp_million
FROM gdp g
JOIN olympics o ON g.Country = o.Country
WHERE g.year BETWEEN 1992 - 4 AND 1992 + 4
AND g.Country IN ('SPAIN')
""" #4 years before host countries gdp

gdp_df = pd.read_sql(gdp_query, conn)

# Plot GDP over 4 years for all host countries
plt.figure(figsize=(10,6))
southkorea_df = gdp_df[gdp_df['Country'] == 'SPAIN']
plt.plot(
    southkorea_df['year'],
    southkorea_df['total_gdp_million'],
    marker='o',
    color='green',
    label='SPAIN'
)

plt.xlabel('Year')
plt.ylabel('Total GDP (Million)')
plt.title('GDP of Spain: 4 Years before and after the 1992 Olympics')
plt.legend()
plt.tight_layout()
plt.savefig('gdp_spain.png')




# Example 2: Medals vs Unemployment
medal_query = """
SELECT i.country, i.year, i.unemployment, COUNT(o.Medal) AS medals
FROM inflation i
JOIN olympics o ON i.country = o.Country AND i.year = o.Year
WHERE o.Medal != 'No medal'
GROUP BY i.country, i.year, i.unemployment
"""
medal_df = pd.read_sql(medal_query, conn)

# Scatter plot: Medals vs Unemployment
plt.figure(figsize=(8,6))
plt.scatter(medal_df['medals'], medal_df['unemployment'], color='blue')
plt.xlabel('Number of Medals')
plt.ylabel('Unemployment Rate (%)')
plt.title('Medals vs Unemployment')
plt.grid(True)
plt.tight_layout()
plt.savefig('medals_vs_unemployment.png') 
# plt.show()  

# Close connection
conn.close()
