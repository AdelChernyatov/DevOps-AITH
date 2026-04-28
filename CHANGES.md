# CHANGES

## Лабораторная работа: Airflow + Spark

- Обновлен `Dockerfile`:
  - добавлены `procps` и `default-jre` через `apt`;
  - добавлено переключение `USER root`/`USER airflow`;
  - добавлено копирование папки `spark`;
  - установлены `apache-airflow-providers-apache-spark==4.1.1` и `pyspark==3.5.0`.
- Обновлен `docker-compose.yaml`:
  - добавлены сервисы `spark-master` и `spark-worker`;
  - добавлен volume `./spark:/opt/airflow/spark` для Airflow;
  - обновлена зависимость запуска сервисов для корректной очередности.
- Добавлен Spark job:
  - `spark/my_spark_job.py` с использованием `SparkSession`.
- Добавлен новый DAG:
  - `dags/spark_submit_dag.py` с `SparkSubmitOperator` и запуском скрипта из `/opt/airflow/spark/my_spark_job.py`.
- Обновлен `README.md`:
  - добавлены инструкции по сборке/запуску, созданию Spark connection в Airflow, запуску DAG и проверке в Spark UI.
