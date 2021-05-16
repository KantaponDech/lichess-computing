if [ "$#" -ne 1 ]; then
    echo "Usage: ./populate_table.sh  bucket-name"
    exit
fi

BUCKET=$1
echo "Populating Cloud SQL instance chess from gs://${BUCKET}/lichess/..."

# To run mysqlimport and mysql, authorize CloudShell
bash authorize.sh

# the table name for mysqlimport comes from the filename, so rename our CSV files, changing bucket name as needed
counter=0
for FILE in $(gsutil ls gs://${BUCKET}/lichess/raw/lichess*.csv); do
   gsutil cp $FILE chess_games.csv-${counter}
   counter=$((counter+1))
done

# import csv files
MYSQLIP=$(gcloud sql instances describe chess --format="value(ipAddresses.ipAddress)")
mysqlimport --local --host=$MYSQLIP --user=root --ignore-lines=1 --fields-terminated-by=',' --password lichess chess_games.csv-*
rm chess_games.csv-*