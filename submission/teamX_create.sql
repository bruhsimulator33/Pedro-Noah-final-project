DROP TABLE IF EXISTS gdp ;
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Sport;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Participation;

CREATE TABLE gdp (
  Country             VARCHAR(64)   NULL,
  year                INT           NULL,
  total_gdp_million   FLOAT         NULL
);

DROP TABLE IF EXISTS inflation;
CREATE TABLE inflation (
  country              VARCHAR(64) NULL,
  year                 INT         NULL,
  inflation            FLOAT       NULL,
  real_interest        FLOAT       NULL,
  lending_interest     FLOAT       NULL,
  unemployment         FLOAT       NULL,
  income_level         VARCHAR(64) NULL
);

DROP TABLE IF EXISTS olympics ;
CREATE TABLE olympics (
  Country    VARCHAR(64)   NULL,
  Year       INT           NULL,
  Medal      VARCHAR(64)   NULL
);

CREATE TABLE Player (
    player_id INT PRIMARY KEY,
    Name VARCHAR(100),
    Sex CHAR(1)
);

CREATE TABLE Team (
    team_id VARCHAR(3) PRIMARY KEY, 
    Team VARCHAR(100),
    NOC VARCHAR(3)
);

CREATE TABLE Game (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    Year INT,
    Season VARCHAR(10),
    City VARCHAR(100)
);

CREATE TABLE Sport (
    sport_id INT PRIMARY KEY AUTO_INCREMENT,
    Sport VARCHAR(100)
);

CREATE TABLE Event (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    Event VARCHAR(100),
    sport_id INT,
    FOREIGN KEY (sport_id) REFERENCES Sport(sport_id)
);

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

DROP TABLE IF EXISTS Observation;
DROP TABLE IF EXISTS Indicator;
DROP TABLE IF EXISTS Country;


CREATE TABLE Country (
    country_name VARCHAR(100) PRIMARY KEY
    
);

CREATE TABLE Indicator (
    indicator_name VARCHAR(255) PRIMARY KEY
);

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
