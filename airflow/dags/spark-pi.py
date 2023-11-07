import airflow
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 11, 18)
}
with airflow.DAG('ejemplo_pyspark',
                  default_args=default_args,
                  schedule_interval='@once',
                  dagrun_timeout=timedelta(minutes=60),
                  description='use case of sparkoperator in airflow') as dag:
    task_etl = SparkSubmitOperator(
        task_id='pi_spark',
        conn_id='spark',
        #application="local:///opt/spark/examples/jars/spark-examples_2.12-3.1.2.jar",
        application="/opt/spark/examples/jars/spark-examples_2.12-3.1.2.jar",
        application_args=["10"],
        java_class="org.apache.spark.examples.SparkPi",
        total_executor_cores='1',
        executor_memory='1G'
    )