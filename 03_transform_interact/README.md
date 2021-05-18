# 3. Interactive data exploration and Data transformation

The objective is transform UTCDate to separate day month year to each column and add RatingDiff column to calculate rating different of both side but it's not necessary to follow this script it's depend on you how do you transform data.

### Interactive data exploration
* Run the script to Create a dataset in BigQuery and load data into BigQuery

      cd chess/03_transform_interact
      bash load_to_bq.sh <BUCKET-NAME>

### Data transformation
* Copy all data in storage and transform data by transform.py then load to storage into other subfolders and big query

      bash transform.sh <BUCKET-NAME>

* Go to big query to check new table as "tran_chess_games"
* Visit the BigQuery console to query the new table

      SELECT * FROM `<bucket-id>.lichess.trans_chess_games`

* Save the results as a table named lichess
* Start up a Cloud AI Platforms Notebook instance.
* Start a new notebook. Then, copy and paste cells from lichess_pred.ipynb and click Run to execute the code.
* Note that testhypo.sql use for query to test basic hypothesis
