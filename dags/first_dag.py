from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


# Define the Python function to be executed
def print_hello():
    print("Hello, Airflow!")


# Define default arguments
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(1),  # DAG will run from yesterday
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,  # Number of retries if the task fails
    "retry_delay": timedelta(minutes=5),  # Time between retries
}

# Define the DAG
with DAG(
    "first_dag",  # DAG ID
    default_args=default_args,
    description="My first DAG in Airflow",
    schedule_interval=timedelta(days=1),  # Run once a day
    catchup=False,  # Do not perform a backfill
) as dag:

    # Define the task using PythonOperator
    hello_task = PythonOperator(
        task_id="print_hello",  # Task ID
        python_callable=print_hello,  # Python function to execute
    )

# Task dependencies (optional for one task, but added for structure)
hello_task
