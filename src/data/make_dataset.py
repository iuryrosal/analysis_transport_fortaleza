import glob
import pandas as pd

def read_files(files, index, df_array):
    if index >= len(files):
        return pd.concat(df_array, axis = 0)
    else:
        df_temp = function(files[index])
        df_array.append(df_temp)
        return read_files(files, index + 1, df_array)

def make_csv(directory):
    dir_ = directory + "*.xml"
    return glob.glob(dir_)

