from openpyxl.styles import Font, PatternFill, Alignment


def contador_erros():
    erros = {
        'total': 0, 'fornecedor': 0, 'sem_trecho': 0, 'bilhete_incompleto': 0,
        'rloc_duplicado': 0, 'nao_preenchido': 0, 'bilhete_duplicado': 0,
        'bilhete_incompleto': 0, 'contrato_inspirado': 0, 'cobraca_nao_permitida': 0,
        'pagamento_indevido': 0, 'bilhete_conciliado': 0,
        'caracter_invalido': 0, 'alterada_baixa': 0, 'cliente_sem_contrato': 0
    }

    return erros


def custom_guia(guia, a, b, cor, font='FFFFFFFF'):
    for cell in guia[a:b]:
        for c in cell:
            c.fill = PatternFill(start_color=cor,
                                 end_color=cor,
                                 fill_type='solid')
            c.font = Font(color=font, bold=True)
            c.alignment = Alignment(horizontal='center')
