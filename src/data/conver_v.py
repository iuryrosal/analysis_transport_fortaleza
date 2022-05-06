import xml.etree.ElementTree as ET
import pandas as pd

def convert_v_file(file):
    tree = ET.parse(file)
    root = tree.getroot()

    df = pd.DataFrame(columns=['data_hora', 'matricula', 'numero_linha', 'numero_veiculo'])


    for movimento in root.findall('Movimentos'):
        for movimento_d in movimento.findall('MovimentoDiario'):
            for categoria in movimento_d.findall('Categoria'):
                for empresa in categoria.findall('Empresa'): 
                    for veiculo in empresa.findall('Veiculo'):
                        num_veiculo = veiculo.get('Numero')
                        for linha in veiculo.findall('Linha'):
                            num_linha = linha.get('Numero')
                            for viagem in linha.findall('Viagem'):
                                for passageiro in viagem.findall('Passageiro'):
                                    df = df.append({'data_hora': passageiro.get('data_hora'),
                                            'matricula': passageiro.get('Matricula'),
                                            'numero_linha': num_linha,
                                            'numero_veiculo': num_veiculo},ignore_index=True)


    return df