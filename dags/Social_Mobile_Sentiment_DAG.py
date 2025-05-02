# Triggering redeploy with schedule update

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Import your actual processing functions
from fetch_reddit import fetch_reddit_data
from fetch_youtube import fetch_youtube_data
from clean_and_sentiment import clean_and_analyze
from combine_export import export_csv

default_args = {
    'owner': 'neha_bharath',
    'start_date': datetime(2024, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='Social_Mobile_Sentiment_DAG',
    default_args=default_args,
    description='Automated Social Sentiment Analysis using Reddit and YouTube',
    schedule_interval='0 */3 * * *',
    catchup=False
)

# Define the tasks
task1 = PythonOperator(
    task_id='fetch_reddit',
    python_callable=fetch_reddit_data,
    dag=dag
)

task2 = PythonOperator(
    task_id='fetch_youtube',
    python_callable=fetch_youtube_data,
    dag=dag
)

task3 = PythonOperator(
    task_id='clean_and_analyze',
    python_callable=clean_and_analyze,
    dag=dag
)

task4 = PythonOperator(
    task_id='export_results',
    python_callable=export_csv,
    dag=dag
)
# Set the order of execution
[task1, task2] >> task3 >> task4
