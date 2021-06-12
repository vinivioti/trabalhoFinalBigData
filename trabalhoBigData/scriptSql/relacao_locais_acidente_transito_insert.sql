INSERT OVERWRITE TABLE relacao_locais_acidente_transito_orc SELECT
	n_boletim,
	data_boletim,
	n_municipio,
	nome_municipio,
	seq_logradouros,
	n_logradouro,
	tipo_logradouro,
	nome_logradouro,
	tipo_logradouro_anterior,
	nome_logradouro_anterior,
	n_bairro,
	nome_bairro,
	tipo_bairro,
	descricao_tipo_bairro,
	n_imovel,
	n_imovel_proximo
FROM relacao_locais_acidente_transito