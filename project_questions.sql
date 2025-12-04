/* ---------------------------------------------
Question 1:
How do the Summer Olympics affect the GDP of a country's host city in the 4 years leading up?
----------------------------------------------*/
SELECT g.country,g.year,g.total_gdp_million,
h.year AS hosts
FROM gdp g
JOIN hosts h
    ON g.country = h.country
WHERE g.year BETWEEN h.year - 4 AND h.year + 4
ORDER BY g.country, g.year;

/* ---------------------------------------------
Question 2:
How do the results of the Summer Olympics affect the winning teams unemployment rate (most medals)?
----------------------------------------------*/
SELECT 
    i.country, 
    i.year,
    i.unemployment AS unemployment_rate
FROM inflation i
JOIN (
    SELECT m1.country, m1.year
    FROM (
        SELECT UPPER(country) AS country, year, COUNT(*) AS medal_count
        FROM olympics
        WHERE medal != 'No medal'
        GROUP BY country, year
    ) m1
    JOIN (
        SELECT year, MAX(medal_count) AS max_medals
        FROM (
            SELECT country, year, COUNT(*) AS medal_count
            FROM olympics
            WHERE medal != 'No medal'
            GROUP BY country, year
        ) m2
        GROUP BY year
    ) m2 ON m1.year = m2.year AND m1.medal_count = m2.max_medals
) winning_teams
ON UPPER(i.country) = winning_teams.country 
AND i.year = winning_teams.year;


/* ---------------------------------------------
Question 3:
How do the results of the Summer Olympics affect the losing teams unemployment rate (least medals)?
----------------------------------------------*/
SELECT i.country, i.year, i.unemployment
FROM inflation i
JOIN (
    SELECT m1.country, m1.year
    FROM (
        SELECT country, year, COUNT(*) AS medal_count
        FROM olympics
        GROUP BY country, year
    ) m1
    JOIN (
        SELECT year, MIN(medal_count) AS min_medals
        FROM (
            SELECT country, year, COUNT(*) AS medal_count
            FROM olympics
            GROUP BY country, year
        ) m2
        GROUP BY year
    ) m2 ON m1.year = m2.year AND m1.medal_count = m2.min_medals
) losing_teams
ON i.country = losing_teams.country AND i.year = losing_teams.year;


/* ---------------------------------------------
Question 4:
How do the results of the Summer Olympics affect the losing teams GDP (least medals)?
----------------------------------------------*/
SELECT g.country, g.year, g.total_gdp_million
FROM gdp g
JOIN (
    SELECT m1.country, m1.year
    FROM (
        SELECT country, year, COUNT(*) AS medal_count
        FROM olympics
        GROUP BY country, year
    ) m1
    JOIN (
        SELECT year, MIN(medal_count) AS min_medals
        FROM (
            SELECT country, year, COUNT(*) AS medal_count
            FROM olympics
            GROUP BY country, year
        ) m2
        GROUP BY year
    ) m2 ON m1.year = m2.year AND m1.medal_count = m2.min_medals
) losing_teams
ON g.country = losing_teams.country AND g.year = losing_teams.year;


/* ---------------------------------------------
Question 5:
How do the results of the Summer Olympics affect the winning teams GDP (most medals)?
----------------------------------------------*/
SELECT g.country, g.year, g.total_gdp_million
FROM gdp g
JOIN (
    SELECT m1.country, m1.year
    FROM (
        SELECT country, year, COUNT(*) AS medal_count
        FROM olympics
        WHERE medal != 'No medal'
        GROUP BY country, year
    ) m1
    JOIN (
        SELECT year, MAX(medal_count) AS max_medals
        FROM (
            SELECT country, year, COUNT(*) AS medal_count
            FROM olympics
            WHERE medal != 'No medal'
            GROUP BY country, year
        ) m2
        GROUP BY year
    ) m2 ON m1.year = m2.year AND m1.medal_count = m2.max_medals
) winning_teams
ON g.country = winning_teams.country AND g.year = winning_teams.year;


/* ---------------------------------------------
Question 6:
How does the GDP of the host country change 4 years after the Summer Olympics (every Summer Olympic term)?
----------------------------------------------*/
SELECT DISTINCT g.country, g.year, g.total_gdp_million
FROM gdp g
JOIN olympics o
  ON g.country = o.country
WHERE g.year BETWEEN o.year AND o.year + 4
  AND o.year % 4 = 0;  


/* ---------------------------------------------
Question 7:
How does the amount of medals won correlate with a country's GDP growth for that year?
----------------------------------------------*/
SELECT m.country, m.year, m.medal_count, g.total_gdp_million,
       (g.total_gdp_million - LAG(g.total_gdp_million) OVER (PARTITION BY g.country ORDER BY g.year)) / NULLIF(LAG(g.total_gdp_million) OVER (PARTITION BY g.country ORDER BY g.year),0) AS gdp_growth
FROM (
    SELECT country, year, COUNT(*) AS medal_count
    FROM olympics
    WHERE medal != 'No medal'
    GROUP BY country, year
) m
JOIN gdp g
  ON m.country = g.country AND m.year = g.year;