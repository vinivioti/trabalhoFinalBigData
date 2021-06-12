from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sqlContext = SQLContext(sc)

df = sqlContext.sql("select desc_tempo, pavimento, count(*) as num_vitimas from " +
                "relacao_ocorrencia_transito_orc group by desc_tempo, pavimento")

df.coalesce(1).write.format("com.databricks.spark.csv").save("/data/home/resultados_finais/envolvidosTempo.csv")