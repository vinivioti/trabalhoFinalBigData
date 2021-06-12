from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sqlContext = SQLContext(sc)

df = sqlContext.sql("select Embreagues, Cast(avg(Idade) as INT) as media_idade_por_embreagues from relacao_pessoas_acidente_transito_orc group by Embreagues")

df.coalesce(1).write.format("com.databricks.spark.csv").save("/data/home/resultados_finais/mediaEmbreagues.csv")