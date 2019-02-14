import pandas as pd
import numpy as np

"""return the top_x_values most common values of original_df_column of df in order"""
def top_x(df, original_df_column, top_x_values) -> list: 
    return list(df[original_df_column].value_counts().head(top_x_values).index)

df = pd.DataFrame(np.matrix([1,1,1,1,2,2,3,3,3,4,5,5,5,5,5]).T, columns=['n'])

assert top_x(df,'n',3) == [5, 1, 3]
