
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os

default_args = {
    'start_date': datetime(2024, 1, 22),
    'schedule_interval': "10 1 * * *",
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'email': 'example@admin.com'
}

def process_data(input_file_location):
  df = pd.read_csv(input_file_location)
  #To remove all rows with no name column
  df = df.dropna(subset=['name'])
  #To split name column up into first_name and last_name columns
  df['name'] = df['name'].astype(str)
  df[['first_name', 'last_name']] = df['name'].str.split(' ',n=1, expand = True)
  #To remove prepended zeros from price column, and convert back to numeric type from string
  df['price'] = df['price'].astype(str).str.lstrip('0')
  df['price'] = pd.to_numeric(df['price'], errors = 'coerce')
  #To create the above_100 column
  df['above_100'] = df['price'] > 100
  #To drop the original name column
  df.drop(columns = ['name'], inplace = True)
  original_file_name = os.path.basename(input_file_location)
  output_file_name = f'processed_{original_file_name}'
  output_path = os.path.join('/content/airflow/dags', output_file_name)
  #To output processed CSV files
  df.to_csv(output_path, index = False)


with DAG('section_1_data_pipelines_dag', default_args = default_args) as dag:
  
  process_dataset1_task = PythonOperator(
      task_id = 'process_dataset1_task',
      python_callable = process_data,
      op_kwargs = {'input_file_location': '/content/airflow/dags/dataset1.csv'}
  )

  process_dataset2_task = PythonOperator(
      task_id = 'process_dataset2_task',
      python_callable = process_data,
      op_kwargs = {'input_file_location': '/content/airflow/dags/dataset2.csv'}
  )

process_dataset1_task >> process_dataset2_task
