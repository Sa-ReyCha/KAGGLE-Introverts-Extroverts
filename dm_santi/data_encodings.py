# LIBRARIES: 


import pandas as pd


# CONFIGURATIONS:

# FUNCTIONS:

def yes_no_encoding(df, column):
    """ This function encodes the specified column creating a binarization of 
    no = 0 
    yes = 1
    """
    df_copy = df.copy()

    if column in df_copy.columns:
        if pd.api.types.is_string_dtype(df_copy[column]):
            mapping = {'yes': 1, 'no': 0}
            df_copy[column] = df_copy[column].str.lower().map(mapping)
        else:
            raise ValueError(
                f"Column '{column}' is not a string-like type and cannot be encoded "
                f"as yes/no. Current dtype is '{df_copy[column].dtype}'."
            )
        
    return df_copy


def binary_encoding(df, column, positive_value, negative_value):
    """ This function encodes the specified column creating a binarization of 
    positive_value = 1 
    negative_value = 0
    """
    df_copy = df.copy()

    if column in df_copy.columns:
        if pd.api.types.is_string_dtype(df_copy[column]):
            mapping = {positive_value: 1, negative_value: 0}
            df_copy[column] = df_copy[column].str.lower().map(mapping)
        else:
            raise ValueError(
                f"Column '{column}' is not a string-like type and cannot be encoded "
                f"as binary. Current dtype is '{df_copy[column].dtype}'."
            )
        
    return df_copy
    