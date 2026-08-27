from datetime import datetime

from airflow import DAG
from airflow.decorators import dag
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator


data_file = Dataset("file:///tmp/dataset.txt")


@dag(
    dag_id="producteur_dataset_bash",
    start_date=datetime(2026, 2, 20),
    schedule=None,
    catchup=False,
)
def producteur():

    produire_fichier = BashOperator(
        task_id="produire_fichier",
        bash_command="echo 'hello' > /tmp/dataset.txt",
        outlets=[data_file],
    )

    write_to_file()

producteur_dag = producteur()
