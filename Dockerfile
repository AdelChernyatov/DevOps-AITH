FROM apache/airflow:2.7.1
WORKDIR /opt/airflow
COPY dags/minimal_dag.py /opt/airflow/dags/minimal_dag.py
