BUCKET=$1
bq load --autodetect --replace --source_format=CSV lichess.chess_games gs://${BUCKET}/lichess/lichess*