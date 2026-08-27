from datetime import datetime
from airflow.sdk import DAG, Asset
from airflow.operators.bash import BashOperator


mon_fichier = Asset("file:///tmp/mon_asset.txt")


