import pandas as pd
import numpy as np
import os
#for each date in folder data, merge data and save to file
dates = os.listdir('./data')
merge_data=pd.DataFrame()
dates = dates[:-3]
for date in dates:
    sub_df = pd.read_csv('./data/'+date)
    sub_df['Date'] = date[:-4]
    merge_data = pd.concat([merge_data,sub_df])
merge_data.to_csv('./data/merge_data.csv',index=False)
