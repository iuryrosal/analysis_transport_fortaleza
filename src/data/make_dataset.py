import glob
import pandas as pd

def convert_files(files: list, index: int = 0, df_array: list = []):
    if index >= len(files):
        return pd.concat(df_array, axis = 0)
    else:
        df_temp = function(files[index])
        df_array.append(df_temp)
        return convert_files(files, index + 1, df_array)

def pick_files(directory):
    dir_ = directory + "/*.xml"
    return glob.glob(dir_)