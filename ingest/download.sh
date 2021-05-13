START_MONTH=$1
START_YEAR=$2
END_MONTH=$3
END_YEAR=$4

for YEAR in $(seq $START_YEAR $END_YEAR); do
    for MONTH in $(seq -w $START_MONTH $END_MONTH); do
        wget "https://database.lichess.org/standard/lichess_db_standard_rated_"$YEAR"-"$MONTH".pgn.bz2"
    done
    for MONTH in $(seq -w $START_MONTH $END_MONTH); do
        bzip2 -d "lichess_db_standard_rated_"$YEAR"-"$MONTH".pgn.bz2"
    done
    for MONTH in $(seq -w $START_MONTH $END_MONTH); do
        python extract.py "lichess_db_standard_rated_"$YEAR"-"$MONTH".pgn" "lichess_"$YEAR$MONTH".csv"
    done
done

rm -rf lichess_db_*