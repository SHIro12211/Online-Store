import data_loader
import pandas as pd

data=data_loader.load_data("dataset/processed/sales_data_cleaned.csv", True)
data_2023=data[data.index.year==2023].copy()

def get_col_month(df):
    df_month = df.copy()
    # Extract month from datetime index
    df_month['Month'] = df_month.index.month
    df_month.reset_index(inplace=True)        # Reset index to make 'Date' a column again
    df_month.drop(columns='Date', inplace=True)  # Drop 'Date' since we're using 'Month'
    return df_month
def numeric_to_string_month(serie_month):
    return pd.to_datetime(serie_month, format='%m').dt.strftime('%b')
def generate_gender_col(data):
    data_copy=data.copy()#reuse the same variable for a copy of the data frame
    data_copy['Gender']=data_copy['Female'].apply(lambda x:  'Female' if x else 'Male')#Recreate the gender column
    return data_copy

def get_group_data(data):
    #sales and profit by product category
    df_sales=data[["Product Category", 'Quantity','Total Amount']].groupby("Product Category").sum().reset_index()
    #sales and profit by months for each product category
    df_m=get_col_month(data)
    df_sales_m=df_m[['Month','Product Category', 'Quantity', 'Total Amount']].groupby(['Month', 'Product Category']).sum().reset_index()
    df_sales_m['Month']=numeric_to_string_month(df_sales_m['Month'])
    df=generate_gender_col(data)
    #sales and profit by genders for each product category
    df_gender=df[['Gender','Total Amount', 'Quantity', 'Product Category']].groupby(['Product Category', 'Gender']).sum().reset_index()
    return df_sales, df_sales_m, df_gender