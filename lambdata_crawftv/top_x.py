import pandas as pd


def top_x(df, original_df_column, top_x_values): 
    """
    returns a dataframe with a new column inplace
    """
    assert (type(top_x_values)==int), "top_x_values is not an int"
    assert (top_x_values > 0), "top_x_values needs to be an int greater than 0"
    assert (type(df)==pd.DataFrame), "df needs to be a pandas dataframe"
    assert (original_df_column in df.columns.values), "name of original_df_column not in the DataFrame"
    l = list(df[original_df_column].value_counts().head(top_x_values).index)
    new_column_name = "top_"+str(top_x_values)+"_from_"+str(original_df_column)
    df[new_column_name] = df[original_df_column].apply(lambda x: x in l)
    return df



