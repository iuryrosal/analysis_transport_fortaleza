import xml.etree.ElementTree as ET
import pandas as pd

def convert_gr_file(file):
    tree = ET.parse(file)
    root = tree.getroot()

    data = {"movimento_data_movimento": [],
            "movimento_origem_rastreamento": [],
            "empresa_codigo": [],
            "veiculo_numero": [],
            "ponto_data_hora": [],
            "ponto_tipo": [],
            "ponto_codigo": []}

    index = 0
    for movimento in root.findall("Movimentos"):
            for empresa in movimento.findall("Empresa"):
                    for veiculo in empresa.findall("Veiculo"):
                            for ponto in veiculo.findall("Ponto"):
                                    data["movimento_data_movimento"].append(movimento.get("data_movimento"))
                                    data["movimento_origem_rastreamento"].append(movimento.get("origem_rastreamento"))
                                    
                                    data["empresa_codigo"].append(empresa.get("codigo"))

                                    data["veiculo_numero"].append(veiculo.get("numero"))

                                    data["ponto_data_hora"].append(ponto.get("data_hora"))
                                    data["ponto_tipo"].append(ponto.get("tipo"))
                                    data["ponto_codigo"].append(ponto.get("codigo"))

                                    index = index + 1

    return pd.DataFrame(data)