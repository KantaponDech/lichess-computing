BUCKET=$1
cd ../dataset
gsutil -m cp *.csv gs://${BUCKET}/lichess/raw