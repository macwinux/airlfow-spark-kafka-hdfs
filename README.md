# Spark/Airflow dev container Visual Studio Code

This devcontainer allow you to develop you spark code directly inside the spark master node.
If you want to run any spark code inside src/main/scala, you only need to run  ```sbt run```.
You can also, run ```sbt package``` and create the .jar that then you can run on your spark cluster with ```spark submit```.

This docker compose has other components:
-   hdfs
-   kakfa
-   Airflow

Airflow is running in your ```locahost:9090```.
**One thing that I need to automate is this part**:
- If you want to use airflow with spark, you need to go to Admin, then connections, and modify spark_default connection with:
    - Connection Id: spark
    - Connection Type: Spark
    - Host: spark://spark-master
    - Port: 7077
    - Extra: {}

Then, if you wan to test it, you can run the dag spark-pi.py via web or with commands:
```docker exec -it spark-local-airflow-1 /bin/bash```

You can check the dags list with:

```airflow dags list```

And you can check spark running:

```airflow dags test ejemplo_pyspark```