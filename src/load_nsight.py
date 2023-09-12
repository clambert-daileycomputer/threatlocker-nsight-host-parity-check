import pandas as pd

HOST_KEY = "Device"

def load_nsight(sourcefile="nsight.csv"):
    dataframe = pd.read_csv(sourcefile)
    filtered_df = dataframe.loc[dataframe['OS'].isin(['windows'])]
    return dataframe, sorted(list(dataframe[HOST_KEY]))
