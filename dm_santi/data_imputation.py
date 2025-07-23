# LIBRARIES:

import pandas as pd
import numpy as np


# CONFIGURATIONS:


# FUNCTIONS:


def mean_imputation(df_train, column, df_test=None):
    """
    Imputes missing values in specified column(s) of training and optionally testing DataFrames.

    The mean for imputation is calculated *only* from the training set and then
    applied to both the training and testing sets (if provided) to prevent data leakage.

    Parameters
    ----------
    df_train : pd.DataFrame
        The training DataFrame with missing values.
    column : str or 'all'
        The column name to impute, or 'all' to impute all numeric columns.
    df_test : pd.DataFrame, optional
        The testing DataFrame with missing values. If provided, it will also be imputed.

    Returns
    -------
    pd.DataFrame or tuple[pd.DataFrame, pd.DataFrame]
        If df_test is provided, returns a tuple of (df_train_imputed, df_test_imputed).
        If df_test is not provided, returns only df_train_imputed.
    """
    df_train_imputed = df_train.copy()
    mean_values = {}
    cols_to_impute = []

    # Column selection
    if column == 'all':
        cols_to_impute = df_train_imputed.select_dtypes(include=np.number).columns.tolist()
    else:
        if column not in df_train_imputed.columns:
            raise ValueError(f"Column '{column}' does not exist in the training DataFrame.")
        if not pd.api.types.is_numeric_dtype(df_train_imputed[column]):
            raise ValueError(f"Column '{column}' is not numeric and cannot be imputed with mean.")
        cols_to_impute = [column]

    # Imputation
    for col in cols_to_impute:
        mean_values[col] = df_train_imputed[col].mean()
        df_train_imputed[col] = df_train_imputed[col].fillna(mean_values[col])
    if df_test is not None:
        df_test_imputed = df_test.copy()
        for col, mean_val in mean_values.items():
            if col in df_test_imputed.columns:
                df_test_imputed[col] = df_test_imputed[col].fillna(mean_val)
        return df_train_imputed, df_test_imputed

    return df_train_imputed



def mode_imputation(df_train, column, df_test=None):
    """
    Imputes missing values in specified column(s) of training and optionally testing DataFrames.

    The mode for imputation is calculated *only* from the training set and then
    applied to both the training and testing sets (if provided) to prevent data leakage.

    Parameters
    ----------
    df_train : pd.DataFrame
        The training DataFrame with missing values.
    column : str or 'all'
        The column name to impute, or 'all' to impute all categorical/object columns.
    df_test : pd.DataFrame, optional
        The testing DataFrame with missing values. If provided, it will also be imputed.

    Returns
    -------
    pd.DataFrame or tuple[pd.DataFrame, pd.DataFrame]
        If df_test is provided, returns a tuple of (df_train_imputed, df_test_imputed).
        If df_test is not provided, returns only df_train_imputed.
    """
    df_train_imputed = df_train.copy()
    mode_values = {}
    cols_to_impute = []

    # Column selection
    if column == 'all':
        # Select object, category, and string dtypes for mode imputation
        cols_to_impute = df_train_imputed.select_dtypes(include=['object', 'category', 'string']).columns.tolist()
    else:
        if column not in df_train_imputed.columns:
            raise ValueError(f"Column '{column}' does not exist in the training DataFrame.")
        col_dtype = df_train_imputed[column].dtype
        if not (pd.api.types.is_object_dtype(col_dtype) or
                pd.api.types.is_string_dtype(col_dtype) or
                pd.api.types.is_categorical_dtype(col_dtype)):
            raise ValueError(f"Column '{column}' is not of a suitable type (object, string, or category) and cannot be imputed with mode. Current dtype is '{col_dtype}'.")
        cols_to_impute = [column]

    # Imputation
    for col in cols_to_impute:
        # Calculate mode only if there are non-NA values to avoid errors
        if df_train_imputed[col].notna().any():
            mode_value = df_train_imputed[col].mode()[0]
            mode_values[col] = mode_value
            df_train_imputed[col] = df_train_imputed[col].fillna(mode_value)
    
    if df_test is not None:
        df_test_imputed = df_test.copy()
        for col, mode_val in mode_values.items():
            if col in df_test_imputed.columns:
                df_test_imputed[col] = df_test_imputed[col].fillna(mode_val)
        return df_train_imputed, df_test_imputed

    return df_train_imputed


# PIPELINE: 
