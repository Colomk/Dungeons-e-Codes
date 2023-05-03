meses_por_extenso = {
    '/01/': 'Janeiro', '/02/': 'Fevereiro', '/03/': 'Março',
    '/04/': 'Abril', '/05/': 'Maio', '/06/': 'Junho',
    '/07/': 'Julho', '/08/': 'Agosto', '/09/': 'Setembro',
    '/10/': 'Outubro', '/11/': 'Novembro', '/12/': 'Dezembro'
}

lancamento_manual = [
    'Reserva importada via planilh',
    'obs', 'Venda importada pela captura de reserva no Middleware!',
    'SOLICITAÇÃO FEITA PELO EMERGENCIAL', 'Código do emissor SP_I_I',
    '.C criado pela equipe da conciliação aérea para ajuste na forma de pagamento e recebimento',
    'Bagagem', 'CONTABILIZAÇÃO BAGAGEM', 'NAO TEM NO GOVER',
    'Reemissão', 'Pet', 'LA*MUILLC', 'SOLICITANTE: MARCELO',
    'COMPRA DE BAGAGEM EXTRA', 'HOTEL', 'CONTABILIZAÇÃO DE ALTERAÇÃO',
    'ASSENTO GOL MAIS CONFORTO', 'Assento', 'Referente compra de bagagem', 'Compra de bagagem',
    'PNR gerado via WebServic', 'QueroPassagem', 'LA*', 'despesas kontik', 'Não integrou', 'bag extra',
    'ASSENTO GOL+CONFORTO', 'ASSENTO CONFORTO','REEMISSAO'
]

list_erros = {
    "bilhete_incompleto": "Bilhete incompleto",
    "caracter_invalido": "Caractere inválido",
    "cliente_sem_contrato": "Cliente sem contrato de fornecedor",
    "cobraca_nao_permitida": "Pagamento não permitido para cobrança",
    "conciliacao_cartao": "Conciliação de Cartão",
    "contrato_inspirado": "Contrato de fornecedor Inspirado",
    "fornecedor": "Falta de Fornecedor",
    "info_gerencial": "Falta de informação Gerencial",
    "nao_indentificado": "Não identificado",
    "pagamento_indevido": "Forma de Pagamento indevida",
    "reprocessar_venda": "Reprocessar Venda",
    "rloc_duplicado": "Duplicidade de RLOC",
    "sem_trecho": "Accounting sem trecho",
    "tarifa_incorreta": "Valores da Tarifa",
    "bilhete_duplicado": "Bilhete duplicado",
    "bilhete_conciliado": "Bilhete conciliado",
    'acc_duplicado': 'Accounting duplicado',
    'alterada_baixa': 'Alteração após baixa',
    'venda_sem_pagamento': 'Venda sem a forma de pagamento/recebimento'
}

erros_msg = {
    "Bilhete deve ter 10 caracteres! (ACC01) ": "Bilhete incompleto",
    "Bilhete deve ter 10 caracteres! (ACC02) ": "Bilhete incompleto",
    "Bilhete deve ter 10 caracteres! (ACC03) ": "Bilhete incompleto",
    "Necessário informar o bilhete": "Bilhete incompleto",
    " Bilhete deve ter 10 caracteres! (ACC03) ": "Bilhete incompleto",
    " Módulo Operações    -> Configurações      -> Configurações do sistema turismo        -> Importação das vendas          -> Entradas/Saídas  Para o ": "Caractere inválido",
    "*' is not a valid integer value": "Caractere inválido",
    "'*' is not a valid integer value": "Caractere inválido",
    "<K9_JUSTIFICATIVA>Antecedência Mínima -": "Caractere inválido",
    "A name was started with an invalid character.  Line: 97 <numeroCartaoPg>ZFX6nXZ<=*>ULPM:</numero": "Caractere inválido",
    "A name contained an invalid character.  Line: 97 <numeroCartaoPg>IS]uH_NqhTQ<LWl8</numero": "Caractere inválido",
    "Erro ao processar PNR  | A name was started with an invalid character.  Line: 31 <K9_MATRICULASOLICITANTE>84261</K9_MATRI": "Caractere inválido",
    "Erro ao processar PNR  | Whitespace is not allowed at this location.  Line: 31 <K9_DESPESA>92</K9_DESPESA><K9_VIP>92</K": "Caractere inválido",
    "Erro ao processar PNR  | Whitespace is not allowed at this location.  Line: 31 <K9_UNIDADE>KPMG FINANCIAL RISK & ACTUAR": "Caractere inválido",
    "Erro ao processar PNR  | Whitespace is not allowed at this location.  Line: 31 <K9_VIP>92</K9_VIP><K9_REQUISICAOCUSTOM>": "Caractere inválido",
    "I9'7u^n<0U</numero": "Caractere inválido",
    "Erro ao processar PNR  | Whitespace is not allowed at this location.  Line: 55 <servicoLocalSaida>HOTEL NOVOTEL ITÚ GOL": "Caractere inválido",
    "A name contained an invalid character.  Line: 97 <numeroCartaoPg>=69n<i0'PHgJ^;3</numeroC": "Caractere inválido",
    "A name contained an invalid character.  Line: 241 <numeroCartaoPg>Li/FYX3_'IJ<G?P:</numero": "Caractere inválido",
    "J": "Caractere inválido",
    "Erro ao processar PNR  | A name was started with an invalid character.  Line: 31 <K9_UNIDADE>NATURA</K9_UNIDADE><K9_CENTR": "Caractere inválido",
    "Erro ao processar PNR  | A semi colon character was expected.  Line: 31 <K9_VIP>91</K9_VIP><K9_REQUISICAOCUSTOM>": "Caractere inválido",
    "A name was started with an invalid character.  Line: 97 <numeroCartaoPg>,9hUHN=<(g_IkH)=</numero": "Caractere inválido",
    "A name was started with an invalid character.  Line: 97 <numeroCartaoPg>o[3?W<5/?1gRUin0</numero": "Caractere inválido",
    "A name contained an invalid character.  Line: 97 <numeroCartaoPg>95i*G0n<g:2jh.LU</numero": "Caractere inválido",
    "Erro ao processar PNR  | A semi colon character was expected.  Line: 31 <K9_VIP>92</K9_VIP><K9_BREAK1>Pet Nutrit": "Caractere inválido",
    "Erro ao processar PNR  | A name was started with an invalid character.  Line: 31 <K9_MATRICULASOLICITANTE>87099</K9_MATRI": "Caractere inválido",
    "<K9_JUSTIFICATIVA>Antecedência Mínima - ": "Caractere inválido",
    "Necessário cadastrar um contrato para o cliente": "Cliente sem contrato de fornecedor",
    "Este cliente não possui permissão para usar este tipo de pagamento e recebimento para este produto.": "Pagamento não permitido para cobrança",
    "05.09.xls": "Conciliação de Cartão",
    "8.09.xls": "Conciliação de Cartão",
    "Não foi possível encontrar um contrato válido para o fornecedor": "Contrato de fornecedor Inspirado",
    "Necessário informar a filial do cliente": "Contrato de fornecedor Inspirado",
    "Fornecedor não preenchido! (ACC01)": "Falta de Fornecedor",
    "Fornecedor não preenchido! (ACC01) Cliente não preenchido! (ACC01)": "Falta de Fornecedor",
    "Fornecedor não preenchido! (ACC02)": "Falta de Fornecedor",
    "Fornecedor não preenchido! (ACC03)": "Falta de Fornecedor",
    "Centro de custo não preenchido! (ACC02) Fornecedor não preenchido! (ACC03)": "Falta de Fornecedor",
    " Broker não preenchido! (ACC02) E-mail do solicitante não preenchido! (ACC02) ": "Falta de informação Gerencial",
    " Canal de venda não preenchido! (ACC03)": "Falta de informação Gerencial",
    " Centro de custo nã": "Falta de informação Gerencial",
    " Centro de custo não preenchido! (ACC02) Empenho/depart": "Falta de informação Gerencial",
    " Centro de custo não preenchido! (ACC02) Nível funcionário": "Falta de informação Gerencial",
    " Centro de custo não preenchido! (ACC03) Verificação d": "Falta de informação Gerencial",
    " E-mail do solicitante não preenchido! (ACC02) ": "Falta de informação Gerencial",
    " Finalidade pré-definida não preenchida! (ACC02) ": "Falta de informação Gerencial",
    "ail do solicitante não preenchido! (": "Falta de informação Gerencial",
    "ail do solicitante não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "ail do solicitante não preenchido! (ACC01) Reason code não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "ail do solicitante não preenchido! (ACC02) ": "Falta de informação Gerencial",
    "Aprovador não preenchido! (ACC01) Broker não preenchido! (ACC01) Matrícula aprovador não preenchida! (ACC01) Matrícula solicitante não preenchida! ": "Falta de informação Gerencial",
    "Broker não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC01) Finalidade não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC01) Finalidade não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Reason code não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC01) OS não preenchida! (ACC01) Projeto não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Break1 não preenchido! (ACC01) Break2 não preenchido! (ACC01) Break3 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Break1 não preenchido! (ACC01) Break2 não preenchido! (ACC01) Break3 não preenchido! (ACC01) Udid1 não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Break1 não preenchido! (ACC01) Break2 não preenchido! (ACC01) Break3 não preenchido! (ACC01) Udid2 não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Break3 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Broker não preenchido! (ACC01) Divisão não preenchida! (ACC01) Divisão não preenchida! (ACC01) Break1 não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Canal de venda não preenchido! (ACC01) Departamento não preenchido! (ACC01) Break1 não preenchido! ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Canal de venda não preenchido! (ACC01) Divisão não preenchida! (ACC01) Divisão não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Canal de venda não preenchido! (ACC01) Finalidade não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) CPF Passageiro não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Departamento não preenchido! (ACC01) Break1 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Divisão não preenchida! (ACC01) Divisão não preenchida! (ACC01) Break1 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Divisão não preenchida! (ACC01) Divisão não preenchida! (ACC01) Projeto não preenchido! (ACC01) Reason ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Convidado não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Projeto não preenchido! ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Informação referencial não preenchida! (ACC01) Requisição ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Nível funcionário não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Requisição não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Requisição não preenchida! (ACC01) Canal de venda não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Requisição não preenchida! (ACC01) Finalidade não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Tarifa máxima não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Tarifa máxima não preenchida! (ACC01) Finalidade não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Finalidade não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Finalidade não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação de controle não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação de controle não preenchida! (ACC01) Broker não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação de controle não preenchida! (ACC01) Matrícula não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação de controle não preenchida! (ACC01) Matrícula não preenchida! (ACC01) Referencial2 não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação referencial 2 não preenchida! (ACC01) Convidado não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação referencial não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação referencial não preenchida! (ACC01) Informação referencial 2 não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Informação referencial não preenchida! (ACC01) Referencial2 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Motivo não preenchido! (ACC01) Break1 não preenchido! (ACC01) Break2 não preenchido! (ACC01) Break3 não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Referencial2 não preenchido! (ACC01) Convidado não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Requisição não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Break3 não preenchido! (ACC02) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Bilhete deve ter 10 caracteres! (ACC02) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Finalidade não preenchida! (ACC02) Convidado não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Nível funcionário não preenchido! (ACC02) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Requisição não preenchida! (ACC02) Motivo não preenchido! ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Informação referencial 2 não preenchida! (ACC02) Convidado não preenchido! (ACC02) Bilhete deve ter 10 ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Informação referencial não preenchida! (ACC02)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Requisição não preenchida! (ACC02)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC04)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC04) Empenho/departamento": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC04) Empenho/departamento não preenchido! (ACC04)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC05) Empenho/departamento não preenchido! (ACC05) Verificação de cam": "Falta de informação Gerencial",
    "Cia mais cara não preenchida! (ACC01) Cia mínima não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Cia mínima não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Cliente não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Cliente passageiro não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Despesa não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "efinida não preenc": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Reason code não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Reason code não preenchido! (ACC01) Unidade não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Udid3 não": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Udid3 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC02) ": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC02) Udid3 não preenchido! (ACC02) ": "Falta de informação Gerencial",
    "Empenho/departamento não pree": "Falta de informação Gerencial",
    "Empenho/departamento não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Empenho/departamento não preenchido! (ACC01) Canal de venda não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Empenho/departamento não preenchido! (ACC01) Canal de venda não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Nível funcionário não ": "Falta de informação Gerencial",
    "Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Nível funcionário não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Nível funcionário não preenchido! (ACC01) Reason code não ": "Falta de informação Gerencial",
    "Finalidade não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Finalidade não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Finalidade não preenchida! (ACC01) Reason code não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Informação de controle não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Informação referencial 2 não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Matrícula não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Nível funcionário não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Número interno não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "OS não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "OS não preenchida! (ACC01) Projeto não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "OS não preenchida! (ACC02) Projeto não preenchido! (ACC02) ": "Falta de informação Gerencial",
    "OS não preenchido! (ACC01)": "Falta de informação Gerencial",
    "OS não preenchido! (ACC01) Projeto não preenchido! (ACC01)": "Falta de informação Gerencial",
    "OS não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Projeto não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Requisição custom não preenchida! (ACC01) Serviço não preenchido! (ACC01) Cliente passageiro não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Solicitante não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Solicitante não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Tarifa máxima excedeu valor permitido! (ACC01) ": "Falta de informação Gerencial",
    "Tarifa máxima não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Tarifa máxima não preenchida! (ACC02)": "Falta de informação Gerencial",
    "Tarifa mínima não pode ser maior que a Tarifa! (ACC01) ": "Falta de informação Gerencial",
    "Tarifa mínima não preenchida! (ACC01) Tarifa máxima não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Tarifa mínima não preenchida! (ACC04) Tarifa máxima não preenchida! (ACC04)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Convidado não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Reason code não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Empenho/departamento não preenchido! (ACC01) Finalidade não preenchida! (ACC01) Nível funcionário não ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC03) Empenho/departamento": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Convidado não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Solicitante não preenchido! (ACC01)": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Udid1 não preenchido! (ACC01) Udid2 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Departamento não preenchido! (ACC01) Projeto não preenchido! (ACC01) Reason code não preenchido! ": "Falta de informação Gerencial",
    "Tarifa mínima não preenchida! (ACC01) Tarifa máxima não preenchida! (ACC01) Bilhete deve ter 10 caracteres! (ACC01) ": "Falta de informação Gerencial",
    "Centro de": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC01) Tarifa máxima não preenchida! (ACC01) Convidado não preenchido! (ACC01)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Requisição não preenchida! (ACC02) Canal de venda não ": "Falta de informação Gerencial",
    " Centro de custo não preenchido! (ACC03)": "Falta de informação Gerencial",
    "efinida não preenchida! (ACC01) Unidade não preenchida! (ACC01) ": "Falta de informação Gerencial",
    "Tarifa máxima excedeu valor permitido! (ACC02) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Informação referencial": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Tarifa máxima não preenchida! (ACC02": "Falta de informação Gerencial",
    "Canal de venda não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Solicitante não preenchido! (ACC02)": "Falta de informação Gerencial",
    "Divisão não preenchida! (ACC01) Divisão não preenchida! (ACC01) Break1 não preenchido! (ACC01) ": "Falta de informação Gerencial",
    "Centro de custo não pree": "Falta de informação Gerencial",
    "Tarifa mínima não preenchida! (ACC01)": "Falta de informação Gerencial",
    "Tarifa máxima não pode ser menor que a Tarifa! (ACC02) ": "Falta de informação Gerencial",
    "Tarifa máxima não pode ser menor que a Tarifa! (ACC04) ": "Falta de informação Gerencial",
    "Centro de custo não preenchido! (ACC02) Empenho/departamento não preenchido! (ACC02) Matrícula não preenchida! (ACC02) Broker não preenchido! ": "Falta de informação Gerencial",
    "23Ocorreu o erro 'Transaction (Process ID 285) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. ": "Não identificado",
    "23Ocorreu o erro 'Violation of PRIMARY KEY constraint 'PK__BB_PNRACCOUNTING__51851410'. Cannot insert duplicate key in object ": "Não identificado",
    "35Ocorreu a seguinte exceção ao gerar a ordem de venda: Ocorreu a seguinte exceção ao inserir a ordem de venda: Ocorreu o erro 'Violation of ": "Não identificado",
    "Empresa do Pcc emissão não encontrada": "Não identificado",
    "Erro ao processar PNR  | Ocorrência no método TBSistemaWrapper.Rollback. Mensagem: This SqlTransaction has completed; it is no longer usable": "Não identificado",
    "Erro ao processar PNR  | Ocorreu o erro 'Transaction (Process ID 344) was deadlocked on lock resources with another process and has been chosen as ": "Não identificado",
    "Erro excluindo PNR: Ocorrência no método TBSistemaWrapper.MyException. Mensagem: Exclusão cancelada devido a vínculo(s) com registros(s) da ": "Não identificado",
    "FINOBJ - Validação do documento: Não é possível incluir este documento porque o(a)": "Não identificado",
    "Matriz/SS": "Não identificado",
    "Microsoft MSXML is not installed": "Não identificado",
    "Ocorreu a seguinte exceção ao gerar a ordem de venda para a accounting: Ocorreu a seguinte exceção ao buscar a configuração do item da ordem de ": "Não identificado",
    "Ocorreu o erro 'Invalid column name 'FATURARSEMCONCILIAR'.' na execução do comando SQL.": "Não identificado",
    "Ocorreu o erro 'Invalid column name 'TIPOPARCELADO'. Invalid column name 'PARCELADOENTRADA'. Invalid column name 'PARCELADOQTD'.' na ": "Não identificado",
    "Ocorreu o erro 'The INSERT statement conflicted with the FOREIGN KEY constraint": "Não identificado",
    "Ocorreu o erro 'Transaction (Process ID 188) was deadlocked on lock resources with another process and has been chosen as the deadlock victim. ": "Não identificado",
    "Ocorreu o erro 'Violation of PRIMARY KEY constraint 'PK__BB_DOCUMENTOINFC__75C27486'. Cannot insert duplicate key in object ": "Não identificado",
    "Postar Venda Não foi possível identificar o vínculo ": "Não identificado",
    "Postar Venda Ocorrência no método TBSistemaWrapper.CreateManagedObject. Mensagem: Arquivo ": "Não identificado",
    " Configurações        -> Configurações do sistema turismo          -> Importação das vendas            -> Impedir vendas com data superior à atual": "Forma de Pagamento indevida",
    " Configurações do sistema Turismo       -> Centros de Custo e Projetos          -> Venda Com as informações:    -> Filial  = Kontik Franstur - Sao ": "Forma de Pagamento indevida",
    "Necessário haver ao menos dois (2) registros de multiplos receb/pagto.": "Forma de Pagamento indevida",
    "Aguarde alguns instantes, esta venda esta sendo processada no momento!": "Reprocessar Venda",
    "Erro ao processar PNR  | Aguarde alguns instantes, esta venda esta sendo processada no momento!": "Reprocessar Venda",
    "Pnr já existente. A duplicidade de rloc é permitida apenas 6 meses após o último pnr emitido": "Duplicidade de RLOC",
    "Não foi possível definir o Local de destino!": "Accounting sem trecho",
    "A soma das tarifas dos registros múltiplos é menor que a tarifa da accounting": "Valores da Tarifa",
    "A soma das tarifas dos registros múltiplos ultrapassa a tarifa da accounting": "Valores da Tarifa",
    "A soma do MarkUp dos registros múltiplos é menor que o MarkUp da accounting": "Valores da Tarifa",

}
