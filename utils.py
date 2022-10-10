from pyspark.conf import SparkConf
from pyspark.sql import SparkSession

def get_spark_session() -> SparkSession:

    conf = SparkConf()

    conf.setAll (
        [
            ("spark.master","spark://0.0.0.0:7077"),
            ("spark.submit.deployMode","client"),
            ("spark.driver.bindAddress","0.0.0.0"),
            ("spark.app.name", "Desafio SICOOPERATIVE"),
            ("spark.driver.extraClassPath","./jars/mysql-connector.jar")
        ]
    )

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    return spark