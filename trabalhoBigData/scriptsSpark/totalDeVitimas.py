from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sqlContext = SQLContext(sc)

df = sqlContext.sql("select l.nome_bairro, count(*) as num_vitimas from " +
                "relacao_pessoas_acidente_transito_orc as p " +
                "INNER JOIN relacao_locais_acidente_transito_orc as l " + 
                "ON p.num_boletim = l.n_boletim where p.Embreagues = 'SIM' group by l.nome_bairro")

df.coalesce(1).write.format("com.databricks.spark.csv").save("/data/home/resultados_finais/totalVitima.csv")
