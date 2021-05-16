BUCKET=$1
gsutil -m cp gs://${BUCKET}/lichess/raw/lichess*.csv .

for FILE in lichess_*.csv; do
    python transform.py $FILE "transformed_"$FILE
done

gsutil -m cp transformed_*.csv gs://${BUCKET}/lichess/transformed

rm -rf *.csv

bq load --autodetect --replace --source_format=CSV lichess.trans_chess_games gs://${BUCKET}/lichess/transformed/transformed*