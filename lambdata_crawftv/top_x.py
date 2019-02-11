import pandas as pd


def top_x(df, new_column, original_df_column, top_x_values):
    top_x_list = list(
        df["original_df_column"].value_counts().head(top_x_values).index)
    df[new_column] = df[original_df_column].apply(lambda x: x in top_x_list)
    return df[new_column]

# top_installers =  x["installer"].value_counts().head(100).index
# top_installers = list(top_installers)
# top_installers.remove('0')
# top_installers
# x["top_installer"] = x["installer"].apply(lambda x : x in top_installers)
