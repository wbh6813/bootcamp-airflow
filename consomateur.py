from airflow.decorators import dag, task
from airflow.datasets import Dataset
from datetime import datetime

data_file = Dataset("/tmp/dataset_asset.txt")


@dag(
    dag_id="consommateur_asset_bash",
    start_date=datetime(2026, 1, 1),
    schedule=[data_file],
    catchup=False,
)
def consommateur_asset_bash():

    @task.bash
    def lire_fichier():
        return "cat /tmp/dataset_asset.txt"

    lire_fichier()


consommateur_dag = consommateur_asset_bash()
