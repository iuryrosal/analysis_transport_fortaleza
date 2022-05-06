import xml.etree.ElementTree as ET
import pandas as pd

def convert_fgr_file(file):
    tree = ET.parse(file)
    root = tree.getroot()

    data = {
            "fechamento_data": [],
            "empresa_numero": [],
            "empresa_nome": [],
            "linha_numero": [],
            "linha_nome": [],
            "linha_km_programado": [],
            "linha_km_adotado": [],
            "linha_eficiencia": [],
            "passageiro_grupo": [],
            "passageiro_demanda": [],
            "passageiro_arrecadacao": [],
            "passageiro_arrecadacao_prevista": []}


    for fechamento in root.findall("Fechamento"):
            for empresa in fechamento.findall("Empresa"):
                    for linha in empresa.findall("Linha"):
                            for arrecadacao in linha.findall("Arrecadacao"):
                                    for passageiro in arrecadacao.findall("Passageiro"):
                                            data["fechamento_data"].append(fechamento.get("dataMovimento"))
                                            
                                            data["empresa_numero"].append(empresa.get("numero"))
                                            data["empresa_nome"].append(empresa.get("nome"))
                                            
                                            data["linha_numero"].append(linha.get("numero"))
                                            data["linha_nome"].append(linha.get("nome"))
                                            data["linha_km_programado"].append(linha.get("kmTotalProgramada"))
                                            data["linha_km_adotado"].append(linha.get("kmAdotada"))
                                            data["linha_eficiencia"].append(linha.get("eficiencia"))
                                            
                                            data["passageiro_grupo"].append(passageiro.get("grupo"))
                                            data["passageiro_demanda"].append(passageiro.get("demanda"))
                                            data["passageiro_arrecadacao"].append(passageiro.get("arrecadacao"))
                                            data["passageiro_arrecadacao_prevista"].append(passageiro.get("arrecadacaoPrevista"))

    return pd.DataFrame(data)