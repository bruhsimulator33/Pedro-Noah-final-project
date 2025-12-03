library(DBI)
library(RMySQL)
library(dplyr)
library(ggplot2)

# Connect to the database
con <- dbConnect(
  MySQL(),
  host = 'db.cs.usna.edu',
  user = 'm270774',
  password = 'm270774',
  dbname = 'm270774'
)

#-----------------------------
# Graph 1: GDP Growth vs Income Level
#-----------------------------
gdp_growth_query <- "
SELECT Country, year, total_gdp_million, incomeLevel
FROM gdp g
JOIN inflation i ON g.Country = i.country AND g.year = i.year
"

gdp_df <- dbGetQuery(con, gdp_growth_query)

# Calculate GDP growth per country
gdp_df <- gdp_df %>%
  arrange(Country, year) %>%
  group_by(Country) %>%
  mutate(gdp_growth = (total_gdp_million - lag(total_gdp_million)) / lag(total_gdp_million) * 100) %>%
  filter(!is.na(gdp_growth))

# Plot GDP growth by income level
ggplot(gdp_df, aes(x = year, y = gdp_growth, color = incomeLevel)) +
  geom_line() +
  labs(title = "GDP Growth by Income Level", x = "Year", y = "GDP Growth (%)") +
  theme_minimal()
ggsave("gdp_growth_income_level_R.png")

#-----------------------------
# Graph 2: Inflation vs Unemployment
#-----------------------------
inflation_query <- "
SELECT country, year, `Inflation, consumer prices (ant rate (%),Lending interest ratenual %)`, `Unemployment, total (% of total labor force) (modeled ILO estimate)` AS unemployment
FROM inflation
WHERE year BETWEEN 2000 AND 2020
"

inflation_df <- dbGetQuery(con, inflation_query)

# Scatter plot: Inflation vs Unemployment
ggplot(inflation_df, aes(x = `Inflation, consumer prices (ant rate (%),Lending interest ratenual %)`, y = unemployment)) +
  geom_point(alpha = 0.6, color = "darkgreen") +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  labs(title = "Inflation vs Unemployment", x = "Inflation Rate (%)", y = "Unemployment Rate (%)") +
  theme_minimal()
ggsave("inflation_vs_unemployment_R.png")

# Close connection
dbDisconnect(con)