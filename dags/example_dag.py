from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Определение DAG
with DAG(
    dag_id="example_dag",
    schedule_interval="@daily",  # Ежедневный запуск
    start_date=datetime(2024, 11, 17),  # Дата начала
    catchup=False,  # Запускать только текущие задачи
    tags=["example"],
) as dag:
    
    # Простые задачи
    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    # Последовательность задач
    start >> end
