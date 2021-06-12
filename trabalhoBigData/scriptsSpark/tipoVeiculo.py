from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sqlContext = SQLContext(sc)

df = sqlContext.sql("select pessoa.especie_veiculo, ocr.pavimento, count(*) as vitimas from " +
                "relacao_ocorrencia_transito_orc as ocr " +
                "INNER JOIN relacao_pessoas_acidente_transito_orc as pessoa ON ocr.n_boletim = pessoa.num_boletim " +
                "group by pessoa.especie_veiculo, ocr.pavimento")

df.coalesce(1).write.format("com.databricks.spark.csv").save("/data/home/resultados_finais/tipoVeiculo.csv")