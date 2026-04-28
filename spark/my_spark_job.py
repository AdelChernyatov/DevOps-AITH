from pyspark import SparkConf
from pyspark.sql import SparkSession


def main() -> None:
    conf = SparkConf().setAppName("airflow_spark_demo").setMaster("spark://spark-master:7077")
    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    data = [("Alice", 10), ("Bob", 20), ("Alice", 5)]
    df = spark.createDataFrame(data, ["name", "value"])
    result = df.groupBy("name").sum("value")

    result.show(truncate=False)
    spark.stop()


if __name__ == "__main__":
    main()
