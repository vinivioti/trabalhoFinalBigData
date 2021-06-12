from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sqlContext = SQLContext(sc)

df = sqlContext.sql("select pessoa.especie_veiculo as especie_veiculo, ocr.desc_tipo_acidente as tipo_acidente, Cast(avg(pessoa.Idade) as INT) as media_idade from " +
                "relacao_ocorrencia_transito_orc as ocr " +
                "INNER JOIN relacao_pessoas_acidente_transito_orc as pessoa ON ocr.n_boletim = pessoa.num_boletim " +
                "group by pessoa.especie_veiculo, ocr.desc_tipo_acidente")

df.coalesce(1).write.format("com.databricks.spark.csv").save("/data/home/resultados_finais/mediaCondutores.csv")