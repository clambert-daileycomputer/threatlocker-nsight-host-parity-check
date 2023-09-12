import pandas as pd

HOST_KEY = "Hostname"

def load_threatlocker(sourcefile="threatlocker.csv"):
    dataframe = pd.read_csv(sourcefile)
    filtered_df = dataframe.loc[dataframe['Group Name'].isin(['Workstations'])]
    return dataframe, sorted(list(filtered_df[HOST_KEY]))