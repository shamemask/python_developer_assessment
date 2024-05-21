from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import json

def validate_response(response):
    if response.status_code != 200:
        raise ValueError(f"Unexpected status code: {response.status_code}")
    data = response.json()
    # Пример проверки: предполагаем, что JSON должен содержать поле 'status'
    if 'status' not in data or data['status'] != 'success':
        raise ValueError("Invalid response data")
    return "Response is valid"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

with DAG(
    'test_api_dag',
    default_args=default_args,
    description='A simple DAG to test an external API',
    schedule_interval=None,
    start_date=days_ago(1),
    tags=['example'],
) as dag:

    test_api_call = SimpleHttpOperator(
        task_id='test_api_call',
        http_conn_id='your_http_conn_id',
        endpoint='very/important/docs',
        method='GET',
        data=json.dumps({"documents_date": {"$gte": "today"}}),
        headers={"Content-Type": "application/json"},
        response_check=lambda response: response.status_code == 200,
        log_response=True,
    )

    validate_api_response = PythonOperator(
        task_id='validate_api_response',
        python_callable=validate_response,
        provide_context=True,
        op_args=['{{ task_instance.xcom_pull(task_ids="test_api_call") }}'],
    )

    test_api_call >> validate_api_response
