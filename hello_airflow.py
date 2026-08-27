from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="hello_airflow",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    hello_task = BashOperator(
        task_id="hello",
        bash_command='echo "Bonjour depuis Airflow"',
    )