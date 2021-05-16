create database if not exists lichess;
use lichess;

drop table if exists chess_games;

create table chess_games(
    EVENTS VARCHAR(100) NOT NULL,
    WHITE VARCHAR(100),
    BLACK VARCHAR(100),
    RESULT VARCHAR(10),
    UTCDATE DATE,
    UTCTIME TIME(0),
    WHITE_ELO INT(5),
    BLACK_ELO INT(5),
    WHITE_RATING_DIFF FLOAT(5),
    BLACK_RATING_DIFF FLOAT(5),
    ECO VARCHAR(10),
    OPENING VARCHAR(500),
    TIME_CONTROL VARCHAR(100),
    TERMINATION VARCHAR(100),
    AN text
);
