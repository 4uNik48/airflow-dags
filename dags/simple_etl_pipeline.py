from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def extract_data():
    # Simulate data extraction
    print("Extracting data...")

def load_data():
    # Simulate loading data
    print("Loading data...")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create DAG
dag = DAG(
    'simple_etl_pipeline',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 11, 16),
    catchup=False,
)

# Define tasks
extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag
)

# Set task dependencies
extract_task >> load_task
