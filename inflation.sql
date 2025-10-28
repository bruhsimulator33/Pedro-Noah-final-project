DROP TABLE IF EXISTS Country;
DROP TABLE IF EXISTS EconomicIndicator;


CREATE TABLE Country (
    country_id CHAR(3) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    iso2c CHAR(2),
    iso3c CHAR(3),
    adminregion VARCHAR(100),
    incomeLevel VARCHAR(50)
);

-- country_name -> iso3c, iso2c, adminregion, incomeLevel
-- The country name determines the codes, regions and income

-- iso3c -> country_name, iso2c, adminregion, incomeLevel
-- iso2c → country_name, iso3c, adminregion, incomeLevel
-- You could also say this since iso2c and iso3c are unique for each country

CREATE TABLE EconomicIndicator (
    country_id CHAR(3) NOT NULL,
    year INT NOT NULL,
    inflation_cpi DECIMAL(10, 2),
    inflation_gdp_deflator DECIMAL(10, 2),
    real_interest_rate DECIMAL(10, 2),
    deposit_interest_rate DECIMAL(10, 2),
    lending_interest_rate DECIMAL(10, 2),
    unemployment_national DECIMAL(10, 2),
    unemployment_ilo DECIMAL(10, 2),


    PRIMARY KEY (country_id, year),  Composite PK (each country can have one record per year)
    FOREIGN KEY (country_id) REFERENCES Country(country_id)
);

-- (country_id, year) - composite key
-- (country_id, year) -> inflation_cpi, inflation_gdp_deflator, real_interest_rate, deposit_interest_rate, lending_interest_rate, unemployment_national, unemployment_ilo
-- for each country in a given year, there is one economic value.