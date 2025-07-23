import pandas as pd

def get_dummy(df, col):
    if col:
        for i in col:
            dummy_variables=pd.get_dummies(df[i])
            df=pd.concat([df,dummy_variables], axis=1)
            df.drop(columns=[i], inplace=True)
    return df

def change_types(df, dtype_map):
    if 'Date' in df.columns:
        try:
            df['Date'] = pd.to_datetime(df['Date'])
        except Exception as e:
            print(f"[Warning] Could not convert 'Date': {e}")
    #change type data
    if dtype_map:
        for col, type in dtype_map.items():
            if col in df.columns:
                df[col] = df[col].astype(type)

def drop_column(df, columns):
    if columns:
        df.drop(columns=columns, inplace=True)

def set_new_index(df, index):
    if index:
        df.set_index(index, inplace=True)
"""
********Main function for data cleansing*********
Parameters: dataframe, a dictionary with the following keys (
{
    'drop_columns': [columns to delete],
    'dtype_dict': {
        'column name': 'data type to change'
        },
    'index': name of the new index,
    'dummy_variables': [column for categorical variables]
}
)
Returns: A dictionary with the following structure:
{
    "success": False or True,
    "message": "...",
    "data": dataframe cleaned or not
}
*************************************************
"""
def clean_data(df, data={}):
    df = df.copy()
    try:
        #get_dummy
        df=get_dummy(df ,data['dummy_variables'])
        #change type column data if exist
        change_types(df, data['dtype_dict'])
        #drop columns
        drop_column(df, data['drop_columns'])
        #set new index
        set_new_index(df,data['index'])

    except KeyError as e:
        return {
            "success": False,
            "message": f"Missing or incorrect key: {e}",
            "data": df
        }
    #check values null
    if df.isnull().values.any():
        return {
            "success": False,
            "message": "There are null values",
            "data": df
        } 
    else:
        return {
            "success": True,
            "message": "Cleaned successfully",
            "data": df
        }
