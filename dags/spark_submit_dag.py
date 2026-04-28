from datetime import datetime

from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


with DAG(
    dag_id="spark_submit_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["spark"],
) as dag:
    SparkSubmitOperator(
        task_id="run_spark_job",
        application="/opt/airflow/spark/my_spark_job.py",
        name="my_spark_job",
        conn_id="spark_local",
        verbose=True,
    )
