import pandas as pd
"""
Loads the scv-type dataset
Parameter: dataset path
Returns: null and prints an error if the dataset is not imported
Or
Returns: the dataset
"""
def load_data(filepath):
    try:
        df=pd.read_csv(filepath)
    except Exception as e:
        print(e)
        return None
    else:
        return df