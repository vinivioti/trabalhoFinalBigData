DROP TABLE relacao_pessoas_acidente_transito_orc;
CREATE EXTERNAL TABLE IF NOT EXISTS relacao_pessoas_acidente_transito_orc (
	num_boletim 			String,
	data_hora_boletim		String,
	n_envolvido				Integer,
	condutor				String, 
	cod_severidade			Integer,
	desc_severidade			String,
	sexo					String,
	cinto_seguranca			String,
	Embreagues				String,
	Idade					Integer,
	nascimento				String,
	categoria_habilitacao	String,
	descricao_habilitacao	String,
	declaracao_obito		Integer,
	cod_severidade_antiga	Integer,
	especie_veiculo			String,
	pedestre				String,
	passageiro				String
)
COMMENT 'Relação de pessoas envolvidas em acidentes de trânsito'
STORED AS ORC;