import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


conn = mysql.connector.connect(
    host='db.cs.usna.edu',
    user='m270774',
    password='m270774',
    database='m270774'
)

gdp_query = """
SELECT g.Country, g.year, g.total_gdp_million
FROM gdp g
JOIN olympics o ON g.Country = o.Country
WHERE g.year BETWEEN o.Year - 4 AND o.Year
"""
gdp_df = pd.read_sql(gdp_query, conn)

# Plot GDP over 4 years for all host countries
plt.figure(figsize=(10,6))
for country in gdp_df['Country'].unique():
    df_country = gdp_df[gdp_df['Country'] == country]
    plt.plot(df_country['year'], df_country['total_gdp_million'], marker='o', label=country)

plt.xlabel('Year')
plt.ylabel('Total GDP (Million)')
plt.title('GDP of Olympic Host Countries 4 Years Leading Up to Olympics')
plt.legend()
plt.tight_layout()
plt.savefig('gdp_host_countries.png')  # save as PNG
# plt.show()  

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
