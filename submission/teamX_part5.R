library(DBI)
library(RMySQL)
library(dplyr)
library(ggplot2)


con <- dbConnect(
  RMySQL::MySQL(),
  host = "db.cs.usna.edu",
  user = "m270978",
  password = "m270978",
  dbname = "m270978"
)



top_country_query <- "
SELECT Country, COUNT(Medal) AS medals
FROM olympics
WHERE Medal != 'No medal'
GROUP BY Country
ORDER BY medals DESC
LIMIT 1;
"

top_country <- dbGetQuery(con, top_country_query)
top_country_name <- top_country$Country[1]

cat('Top medal country:', top_country_name, '\n')



gdp_query <- sprintf("
SELECT Country, year, total_gdp_million
FROM gdp
WHERE Country = '%s'
ORDER BY year;
", top_country_name)

gdp_df <- dbGetQuery(con, gdp_query)



png("gdp_top_country.png", width = 1600, height = 1000, res = 150)
print(
  ggplot(gdp_df, aes(x = year, y = total_gdp_million)) +
    geom_line(color = 'darkgreen', linewidth = 1.2) +
    geom_point(color = 'black', size = 3) +
    labs(
      title = paste('GDP Over Time for', top_country_name),
      x = 'Year',
      y = 'GDP (Million USD)'
    ) +
    theme_minimal()
)
dev.off()



unemp_query <- sprintf("
SELECT i.country, i.year, i.unemployment, 
       COUNT(o.Medal) AS medals
FROM inflation i
LEFT JOIN olympics o 
  ON i.country = o.Country AND i.year = o.Year AND o.Medal != 'No medal'
WHERE i.country = '%s'
GROUP BY i.country, i.year, i.unemployment
ORDER BY i.year;
", top_country_name)

unemp_df <- dbGetQuery(con, unemp_query)



png("unemployment_vs_medals_top_country.png", width = 1600, height = 1000, res = 150)
print(
  ggplot(unemp_df, aes(x = medals, y = unemployment)) +
    geom_point(size = 4, color = 'blue') +
    geom_smooth(method = 'lm', se = FALSE, color = 'red') +
    labs(
      title = paste('Unemployment vs Medal Count for', top_country_name),
      x = 'Medals Won',
      y = 'Unemployment Rate (%)'
    ) +
    theme_minimal()
)
dev.off()


dbDisconnect(con)