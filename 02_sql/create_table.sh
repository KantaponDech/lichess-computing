bash authorize.sh

MYSQLIP=$(gcloud sql instances describe chess --format="value(ipAddresses.ipAddress)")
mysql --host=$MYSQLIP --user=root --password --verbose < create_table.sql
*
