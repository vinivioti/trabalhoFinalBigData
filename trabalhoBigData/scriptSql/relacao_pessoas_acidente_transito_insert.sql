INSERT OVERWRITE TABLE relacao_pessoas_acidente_transito_orc SELECT
	num_boletim,
	data_hora_boletim,
	n_envolvido,
	condutor, 
	cod_severidade,
	desc_severidade,
	sexo,
	cinto_seguranca,
	Embreagues,
	Idade,
	nascimento,
	categoria_habilitacao,
	descricao_habilitacao,
	declaracao_obito,
	cod_severidade_antiga,
	especie_veiculo,
	pedestre,
	passageiro
FROM relacao_pessoas_acidente_transito