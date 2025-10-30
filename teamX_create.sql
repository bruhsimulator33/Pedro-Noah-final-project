

-- GDP TABLES

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




    --INFLATION TABLES



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



--OLYMPICS TABLES

DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Sport;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Participation;


CREATE TABLE Player (
    player_id INT PRIMARY KEY,
    Name VARCHAR(100),
    Sex CHAR(1)
);

-- player_id -> Name and sex
-- each a players name and sex can be determined by the player_id



CREATE TABLE Team (
    team_id VARCHAR(3) PRIMARY KEY, 
    Team VARCHAR(100),
    NOC VARCHAR(3)
);

-- team_id -> Team and NOC
-- team_id determines the Team name and the national olympic committee code.

CREATE TABLE Game (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    Year INT,
    Season VARCHAR(10),
    City VARCHAR(100)
);

-- game_id -> Year, Season and City
-- the game_id determines the Year, Season and city for that game.

CREATE TABLE Sport (
    sport_id INT PRIMARY KEY AUTO_INCREMENT,
    Sport VARCHAR(100)
);

-- sports_id -> sports
-- Sports_id determines the sport being played

CREATE TABLE Event (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    Event VARCHAR(100),
    sport_id INT,
    FOREIGN KEY (sport_id) REFERENCES Sport(sport_id)
);

-- event_id -> event and sport_id
-- each event belongs to a sport and that sport and event is what makes up an event_id

CREATE TABLE Participation (
    participation_id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT,
    event_id INT,
    game_id INT,
    team_id VARCHAR(3),
    Medal VARCHAR(20),
    FOREIGN KEY (player_id) REFERENCES Player(player_id),
    FOREIGN KEY (event_id) REFERENCES Event(event_id),
    FOREIGN KEY (game_id) REFERENCES Game(game_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id)
);

-- participation_id -> player_id, event_id, game_id, team_id, Medal
-- the participation_id is a combination of the player at a specific event for a specific game on a specific team, and possibly winning a medal.