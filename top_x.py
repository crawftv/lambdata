import pandas as pd


def top_x(df, new_column, original_df_column, top_x_values):
    top_x_list = list(
        df["original_df_column"].value_counts().head(top_x_values).index)
    df[new_column] = df[original_df_column].apply(lambda x: x in top_x_list)
    return df[new_column]

