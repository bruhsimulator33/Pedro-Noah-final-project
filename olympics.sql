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

CREATE TABLE olympics_clean (
    Country VARCHAR(50),
    Year INT,
    Medal VARCHAR(50)
);
LOAD DATA INFILE '/path/to/olympics_clean.csv'
INTO TABLE olympics_clean
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;