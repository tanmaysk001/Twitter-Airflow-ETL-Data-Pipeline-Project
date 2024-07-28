from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from scripts.Data_Extraction import extract_tweets
from scripts.Data_Transformation import transform_data
from scripts.Data_Loading import upload_to_s3

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 7, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_twitter_etl():
    df = extract_tweets('python', 100)
    df_transformed = transform_data(df)
    upload_to_s3(df_transformed, 'twitter_data.csv')

with DAG('twitter_etl_dag', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    etl_task = PythonOperator(
        task_id='twitter_etl_task',
        python_callable=run_twitter_etl,
    )
