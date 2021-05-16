# 3. Data transformation

The objective is transform UTCDate to separate day month year to each column and add RatingDiff column to calculate rating different of both side but it's not necessary to follow this script it's depend on you how do you transform data.

## Data transformation
* Copy all data in storage and transform data by transform.py then load to storage into other subfolders and big query

      cd chess/03_transform
      bash transform.sh <BUCKET-NAME>
    
* Go to big query to check new table as "tran_chess_games"
