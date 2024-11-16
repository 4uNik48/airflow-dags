from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Определение DAG
with DAG(
    dag_id='testik_dag',
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
    description='Простой DAG для теста',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:
    # Определение задач
    start_task = DummyOperator(
        task_id='start_task'
    )

    end_task = DummyOperator(
        task_id='end_task'
    )

    # Установление последовательности выполнения
    start_task >> end_task
