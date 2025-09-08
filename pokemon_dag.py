from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from pathlib import Path
import sys

# ================================
# Ensure we can import main.py
# (assumes main.py is in same folder as this dag file)
# If it's in your project folder, adjust path accordingly
# ================================
PROJECT_PATH = Path("/mnt/c/Github/Pokemon")  # adjust if different in WSL
if str(PROJECT_PATH) not in sys.path:
    sys.path.append(str(PROJECT_PATH))

from main import main  # import your main() function

# ================================
# Default arguments for DAG
# ================================
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# ================================
# Define DAG
# ================================
with DAG(
    dag_id="pokemon_pipeline",
    default_args=default_args,
    description="Fetch Pokémon data from API and store into DuckDB",
    schedule_interval="@daily",  # runs once per day
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["pokemon", "duckdb", "api"],
) as dag:

    run_main = PythonOperator(
        task_id="fetch_and_store_pokemon",
        python_callable=main,
    )

    run_main
