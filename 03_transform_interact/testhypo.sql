--Hypothesis 1: The player who have higher rating they will win.
SELECT
(SELECT count(result)
FROM lichess.trans_chess_games
WHERE result = "1-0" AND whiteELO IS NOT NULL AND blackELO IS NOT NULL AND whiteELO > blackELO) as white,

(SELECT count(result)
FROM lichess.trans_chess_games
WHERE result = "0-1" AND whiteELO IS NOT NULL AND blackELO IS NOT NULL AND whiteELO > blackELO) as white_lose,

(SELECT count(result)
FROM lichess.trans_chess_games
WHERE result = "1-0" AND whiteELO IS NOT NULL AND blackELO IS NOT NULL AND whiteELO < blackELO) as black_loss,

(SELECT count(result)
FROM lichess.trans_chess_games
WHERE result = "0-1" AND whiteELO IS NOT NULL AND blackELO IS NOT NULL AND whiteELO < blackELO) as black;