# 1.Ingest data onto cloud

### Create a bucket
* Go to the Storage section of the GCP web console and create a new bucket
* Back to shell and make new directory "dataset" to store downloaded data

### Download data
* Download data from https://database.lichess.org visit this site to see data update in month-period
* In this script run download data, unzip bzip2 file, extract data from .pgn text file and export to .csv file

      bash download.sh <START-MONTH> <START-YEAR> <END-MONTH> <END-YEAR>
      
### Upload to storage bucket
* Upload all extracted data file to storage bucket

      bash upload.sh <BUCKET-NAME>

* Go to storage bucket to check data is appeared in 

      gs://<BUCKET-NAME>/lichess/raw
