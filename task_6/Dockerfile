FROM apache/airflow:2.5.1

USER root
RUN apt-get update && apt-get install -y sudo
USER airflow
RUN pip install --no-cache-dir pandas pydantic apache-airflow-providers-http 'sqlalchemy<2.0'
