import pandas as pd
import numpy as np



def data_loader(path, datatype=None):


  #read data file
  data = pd.read_csv(path)
  # Removing email content from first column
  data = data.drop(columns='Unnamed: 0')
  imput_col = data.columns

  # impute Nan in with max*10 if max is 0 we just put 10
  if  imput_col !=None:
    for col in imput_col:
      if data[col].isna().any():
        max_val = data[col].max()*10
        if max_val == 0:
          max= 10
        data[col] = data[col].mask(data[col].isna(),max_val)
# convert categorical to string dtype     
#   if datatype !=None:
#     for col in datatype:
#       if data[col].dtypes == 'int64':
#         data[col] = data[col].astype(str)
#       else:
#         # we known two column has float so else will convert float to string
#         data[col] = data[col].astype(str)
  return data
        
