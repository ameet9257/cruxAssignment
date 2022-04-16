from unittest import result
import numpy as np
import pandas as pd
from datetime import datetime

#read csv input data to data frame as string
df_input1 = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\input.csv",dtype=str)
df_input2 = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\input.csv",dtype=str)

#Information in the excel file is not consistent. 
# In input File - > All the data in the uppercase
# In Output File -> All the data in the lowercase

#Removing the 'W/E '  string from the date field for converting the field into valid data and comparison with output field the_date
df_input1['PER'] = df_input1['PER'].str.replace('W/E ', '')
df_input1['PER'] = pd.to_datetime(df_input1['PER'])

df_input2['PER'] = df_input1['PER'].str.replace('W/E ', '')
df_input2['PER'] = pd.to_datetime(df_input2['PER'])

#extracting month and year data and adding to the new dataframe 
df_input1["per_year_month_input1"]=pd.to_datetime(df_input1['PER']).dt.year.astype(str)+"-"+df_input1['PER'].dt.month.astype(str)
df_input2["per_year_month_input2"]=(pd.to_datetime(df_input2['PER']).dt.year-1).astype(str)+"-"+df_input2['PER'].dt.month.astype(str)

#Joining output dataframe with input dataframe based on the ke columns
df_outout_input = df_output.merge(df_input, 
                    left_on=['MKT','PROD','CP-CATEGORY','CP-MANUFACTURER','CP-FRANCHISE','CP-BRAND','CP-SUBBRAND','CP-SUBBRAND VARIANT','CP-PRICE TIER','CP-SEGMENT',
                    'per_year_month_input1'],
                    right_on=['MKT','PROD','CP-CATEGORY','CP-MANUFACTURER','CP-FRANCHISE','CP-BRAND','CP-SUBBRAND','CP-SUBBRAND VARIANT','CP-PRICE TIER','CP-SEGMENT',
                    'per_year_month_input2'],
                    how='left',suffixes=('_left','_right')
)


#Select only necessary dimension and measures from both data set. 
#df_outout_input = df_outout_input[output_col]
#df_outout_input.to_csv(r'C:\EDC\Other\cruxAssignment\outputFiles\output_transform.csv', index=False)
print(df_outout_input.head)
