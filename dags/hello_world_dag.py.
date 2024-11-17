from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Функция, которая будет выполняться в DAG
def hello_world():
    print("Hello, World from Airflow!")

# Определяем DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hello_world_dag',  # Имя DAG
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=timedelta(days=1),  # Расписание: запуск раз в сутки
    start_date=datetime(2023, 1, 1),  # Дата начала
    catchup=False,  # Не запускать пропущенные задачи
) as dag:
    # Определяем задачу
    task_hello_world = PythonOperator(
        task_id='print_hello',  # Уникальный ID задачи
        python_callable=hello_world,  # Указываем функцию для выполнения
    )

# Задачи в этом DAG идут последовательно, но в данном случае одна задача.
