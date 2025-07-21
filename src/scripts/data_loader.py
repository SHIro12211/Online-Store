import pandas as pd
"""
Loads the scv-type dataset
Parameter: dataset path
Returns: null and prints an error if the dataset is not imported
Or
Returns: the dataset
"""
def load_data(filepath, index_date=None):
    try:
        if index_date:
            df=pd.read_csv(filepath, index_col=0, parse_dates=True)
        else:
            df=pd.read_csv(filepath)
    except Exception as e:
        print("We can't execute that: ",e)
        return None
    else:
        return df