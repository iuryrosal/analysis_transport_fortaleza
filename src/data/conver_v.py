import xml.etree.ElementTree as ET
import pandas as pd

def convert_v_file(file):
    tree = ET.parse(file)
    root = tree.getroot()

    data = {
            "movimentos_data_arq": [],
            "movimento_diario_data_mov": [],
            "categoria_tipo": [],
            "empresa_codigo": [],
            "empresa_modalidade": [],
            "veiculo_numero": [],
            "veiculo_validador": [],
            "linha_numero": [],
            "linha_jornada": [],
            "linha_num_operador": [],
            "linha_tabela": [],
            "linha_hora_abertura": [],
            "linha_hora_fechamento": [],
            "viagem_data_hora_abertura": [],
            "viagem_data_hora_fechamento": [],
            "viagem_catraca_inicio": [],
            "viagem_catraca_final": [],
            "viagem_sentido": [],
            "viagem_ponto_abertura": [],
            "viagem_ponto_fechamento": [],
            "passageiro_data_hora": [],
            "passageiro_integracao_bum": [],
            "passageiro_valor_subsidio": [],
            "passageiro_evento": [],
            "passageiro_sigben": [],
            "passageiro_integracao": [],
            "passageiro_valor_pago": [],
            "passageiro_tipo": [],
            "passageiro_matricula": [],
            "passageiro_valor_repasse_metro": []}

    for movimento in root.findall('Movimentos'):
        for movimento_d in movimento.findall('MovimentoDiario'):
            for categoria in movimento_d.findall('Categoria'):
                for empresa in categoria.findall('Empresa'): 
                    for veiculo in empresa.findall('Veiculo'):
                        for linha in veiculo.findall('Linha'):
                            for viagem in linha.findall('Viagem'):
                                for passageiro in viagem.findall('Passageiro'):
                                    data["movimentos_data_arq"].append(movimento.get("data_arq"))
                                    
                                    data["movimento_diario_data_mov"].append(movimento_d.get("data_mov"))
                                    
                                    data["categoria_tipo"].append(categoria.get("Tipo"))
                                    
                                    data["empresa_codigo"].append(empresa.get("Codigo"))
                                    data["empresa_modalidade"].append(empresa.get("modalidade"))
                                    
                                    data["veiculo_numero"].append(veiculo.get("Numero"))
                                    data["veiculo_validador"].append(veiculo.get("validador"))
                                    
                                    data["linha_numero"].append(linha.get("Numero"))
                                    data["linha_jornada"].append(linha.get("jornada"))
                                    data["linha_num_operador"].append(linha.get("num_operador"))
                                    data["linha_tabela"].append(linha.get("tabela"))
                                    data["linha_hora_abertura"].append(linha.get("hora_abertura"))
                                    data["linha_hora_fechamento"].append(linha.get("hora_fechamento"))
                                    
                                    data["viagem_data_hora_abertura"].append(viagem.get("data_hora_abertura"))
                                    data["viagem_data_hora_fechamento"].append(viagem.get("data_hora_fechamento"))
                                    data["viagem_catraca_inicio"].append(viagem.get("catraca_inicio"))
                                    data["viagem_catraca_final"].append(viagem.get("catraca_final"))
                                    data["viagem_sentido"].append(viagem.get("sentido"))
                                    data["viagem_ponto_abertura"].append(viagem.get("ponto_abertura"))
                                    data["viagem_ponto_fechamento"].append(viagem.get("ponto_fechamento"))
                                    
                                    data["passageiro_data_hora"].append(passageiro.get("data_hora"))
                                    data["passageiro_integracao_bum"].append(passageiro.get("integracao_bum"))
                                    data["passageiro_valor_subsidio"].append(passageiro.get("valor_subsidio"))
                                    data["passageiro_evento"].append(passageiro.get("evento"))
                                    data["passageiro_sigben"].append(passageiro.get("sigben"))
                                    data["passageiro_integracao"].append(passageiro.get("integracao"))
                                    data["passageiro_valor_pago"].append(passageiro.get("valor_pago"))
                                    data["passageiro_tipo"].append(passageiro.get("tipo"))
                                    data["passageiro_matricula"].append(passageiro.get("Matricula"))
                                    data["passageiro_valor_repasse_metro"].append(passageiro.get("valor_repasse_metro"))

    return pd.DataFrame(data)