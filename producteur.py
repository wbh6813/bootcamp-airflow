from datetime import datetime

from airflow.sdk import DAG, Asset
from airflow.providers.standard.operators.bash import BashOperator


mon_asset = Asset("file:///tmp/mon_asset.txt")


# DAG PRODUCTEUR
with DAG(
    dag_id="producteur_asset_bash",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    produire_fichier = BashOperator(
        task_id="produire_fichier",
        bash_command="echo 'hello' > /tmp/mon_asset.txt",
        outlets=[mon_asset],
    )


# DAG CONSOMMATEUR
with DAG(
    dag_id="consommateur_asset_bash",
    start_date=datetime(2026, 1, 1),
    schedule=[mon_asset],
    catchup=False,
) as dag:

    lire_fichier = BashOperator(
        task_id="lire_fichier",
        bash_command="cat /tmp/mon_asset.txt",
    )