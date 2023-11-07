FROM apache/airflow:2.7.2
USER root
RUN apt-get update && apt-get install -y iputils-ping
RUN apt-get update && apt-get install -y wget
ARG SPARK_URL=https://archive.apache.org/dist/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz
RUN wget -O /tmp/spark.tgz $SPARK_URL
RUN tar -C /tmp -zxvf /tmp/spark.tgz
RUN mkdir -p /opt/spark /opt/spark/eventlog
RUN mv /tmp/spark-*/* /opt/spark
RUN apt-get update && apt-get install -y default-jdk
ENV JAVA_HOME="/usr/lib/jvm/java-1.11.0-openjdk-amd64"
ENV AIRFLOW_CONN_SPARK_DEFAULT="spark://spark-master:7077"
ENV PATH=$PATH:$JAVA_HOME/bin
USER airflow
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --no-cache-dir apache-airflow-providers-apache-spark==4.2.0
ENV SPARK_HOME='/opt/spark'
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
CMD [ "standalone" ]