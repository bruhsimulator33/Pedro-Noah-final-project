DROP TABLE IF EXISTS Observation;
DROP TABLE IF EXISTS Indicator;
DROP TABLE IF EXISTS Country;


CREATE TABLE Country (
    country_name VARCHAR(100) PRIMARY KEY
    
);

-- country_name -> the rest of the attributes

CREATE TABLE Indicator (
    indicator_name VARCHAR(255) PRIMARY KEY
);

-- indicator_name -> the rest of the attributes

CREATE TABLE Observation (
    country_name VARCHAR(100) NOT NULL,
    indicator_name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    value DECIMAL(15, 4),

    -- composite
    PRIMARY KEY (country_name, indicator_name, year),

    -- Foreign Keys
    FOREIGN KEY (country_name) REFERENCES Country(country_name),
    FOREIGN KEY (indicator_name) REFERENCES Indicator(indicator_name)
    );

    -- (country_name, indicator_name, year) -> value
    -- for a country name with an indicator name and a year, there is only one value.
    -- you cannot deetermine the value without the entire composite key