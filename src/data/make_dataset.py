import glob
import pandas as pd
from psutil import disk_partitions
from conver_gr import convert_gr_file
from conver_v import convert_v_file
from conver_fgr import convert_fgr_file
import logging

logging.basicConfig(filename = "log_processamento.log",
                    level = logging.DEBUG,
                    format = "%(asctime)s :: %(message)s :: %(levelno)s :: %(lineno)d")

def convert_files(files: list, index: int = 0, df_array: list = [], type_file = "gr"):
    if index >= len(files):
        return pd.concat(df_array, axis = 0)
    else:
        logging.info("Processando: " + files[index])
        if type_file == "gr":
            df_temp = convert_gr_file(files[index])
            file_type = 'gr'
        elif type_file == "v":
            df_temp = convert_v_file(files[index])
            file_type = 'v'
        else:
            df_temp = convert_fgr_file(files[index])

        df_array.append(df_temp)
        return convert_files(files, index + 1, df_array, file_type)

def pick_files(directory):
    return glob.glob(directory)

def make_dataset():
    #logging.info("Processamento GR Iniciado")
    #files = pick_files("../../data/raw/gr/GR_*.xml")
    #df_gr = convert_files(files = files,
    #                      type_file="gr")
    #df_gr.to_csv("../../data/processed/GR.csv")
    #logging.info("Processamento GR Concluído")

    logging.info("Processamento V Iniciado")
    files = pick_files("../../data/raw/v/V*.xml")
    df_gr = convert_files(files = files,
                          type_file="v")
    df_gr.to_csv("../../data/processed/V.csv")
    logging.info("Processamento V Concluído")

    logging.info("Processamento FGR Iniciado")
    files = pick_files("../../data/raw/fgr/FGR*.xml")
    df_gr = convert_files(files = files,
                          type_file="fgr")
    df_gr.to_csv("../../data/processed/FGR.csv")
    logging.info("Processamento FGR Concluído")

make_dataset()