# 2. Creating dashboards

### Loading data into Google Cloud SQL
* Create SQL instance.

      cd chess/02_sql
      bash create_instance.sh

* Go to Cloud SQL instance and change the root password of instance.
* Create table.

      bash create_table.sh
      
* Populate the table.

      bash populate_table.sh <BUCKET-NAME>
      
* Query or Compute as you want such as contingency table then create dashboard on data studio.
