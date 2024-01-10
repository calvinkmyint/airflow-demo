from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def print_hello():
    print("Hello World")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

dag = DAG(
    "hello_world_dag",
    default_args=default_args,
    schedule_interval="0 9 * * *", # Run every day at 9 am
)

# Create the task using the PythonOperator
hello_task = PythonOperator(
    task_id="hello_task",
    python_callable=print_hello,
    dag=dag,
)

# Set the task dependencies (none in this case)
hello_task
