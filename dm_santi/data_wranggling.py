# LIBRARIES: 


import pandas as pd


# CONFIGURATIONS: 


# FUNCTIONS: 

def load_data_2df(file_path):
    """ 
    Loads csv, excel, picke or json files into a dataframe.
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    elif file_path.endswith('.pkl'):
        return pd.read_pickle(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")