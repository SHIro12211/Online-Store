
import pandas as pd
import numpy as np

df=pd.read_csv('dataset/raw/Sales Dataset.csv')

#cleaning data
#drop column Unnamed: 0, because it is not useful 
df.drop(columns=['Unnamed: 0'], inplace=True)
#tranform the colummn Date to datetime
df['Date']=pd.to_datetime(df['Date'])
print(df.info())