from unittest import result
import numpy as np
import pandas as pd
from datetime import datetime

#read csv input data to data frame as string
df_input = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\input.csv",dtype=str)
df_output = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\output.csv",dtype=str)

#Information in the excel file is not consistent. 
# In input File - > All the data in the uppercase
# In Output File -> All the data in the lowercase

#Converting output data as uppercase so that it can be joined
df_output = df_output.apply(lambda x: x.astype(str).str.upper())

#Removing the 'W/E '  string from the date field for converting the field into valid data and comparison with output field the_date
df_input['PER'] = df_input['PER'].str.replace('W/E ', '')
df_input['PER'] = pd.to_datetime(df_input['PER'])

#Converting the string date field to date
df_output["the_date"] = pd.to_datetime(df_output['the_date'])

#extracting month and year data and adding to the new dataframe 
df_input["per_year_month"]=pd.to_datetime(df_input['PER']).dt.year.astype(str)+"-"+df_input['PER'].dt.month.astype(str)
df_output["last_year_month"]=(pd.to_datetime(df_output['the_date']).dt.year-1).astype(str)+"-"+df_output['the_date'].dt.month.astype(str)


#Joining output dataframe with input dataframe based on the ke columns
df_outout_input = df_output.merge(df_input, 
                    left_on=['market','product','category','manufacturer','franchise','brand','subbrand','subbrand_variant','pricetier','segment','last_year_month'],
                    right_on=['MKT','PROD','CP-CATEGORY','CP-MANUFACTURER','CP-FRANCHISE','CP-BRAND','CP-SUBBRAND','CP-SUBBRAND VARIANT','CP-PRICE TIER','CP-SEGMENT',
                    'per_year_month'],
                    how='left',suffixes=('_left','_right')
)

# updatng the all the _ly fields if the data is available for the last year in the inut data fields. 
df_outout_input['dollars_ly'] = np.where((df_outout_input['dollars_ly'] == '0') & (df_outout_input['Dollars'] != '0'), df_outout_input['Dollars'], df_outout_input['dollars_ly'])
df_outout_input['dollar_baseline_ly'] = np.where((df_outout_input['dollar_baseline_ly'] == '0') & (df_outout_input['Baseline $'] != '0'), df_outout_input['Baseline $'], df_outout_input['dollar_baseline_ly'])
df_outout_input['units_ly'] = np.where((df_outout_input['units_ly'] == '0') & (df_outout_input['Units'] != '0'), df_outout_input['Units'], df_outout_input['units_ly'])
df_outout_input['units_baseline_ly'] = np.where((df_outout_input['units_baseline_ly'] == '0') & (df_outout_input['Baseline Units'] != '0'), df_outout_input['Baseline Units'], df_outout_input['units_baseline_ly'])
df_outout_input['dollars_w_ftr_wo_disp_ly'] = np.where((df_outout_input['dollars_w_ftr_wo_disp_ly'] == '0') & (df_outout_input['Dollars w/Ftr w/o Disp'] != '0'), df_outout_input['Dollars w/Ftr w/o Disp'], df_outout_input['dollars_w_ftr_wo_disp_ly'])
df_outout_input['dollars_w_disp_wo_ftr_ly'] = np.where((df_outout_input['dollars_w_disp_wo_ftr_ly'] == '0') & (df_outout_input['Dollars w/Disp w/o Ftr'] != '0'), df_outout_input['Dollars w/Disp w/o Ftr'], df_outout_input['dollars_w_disp_wo_ftr_ly'])
df_outout_input['dollars_w_ftr_and_disp_ly'] = np.where((df_outout_input['dollars_w_ftr_and_disp_ly'] == '0') & (df_outout_input['Dollars w/Ftr  Disp'] != '0'), df_outout_input['Dollars w/Ftr  Disp'], df_outout_input['dollars_w_ftr_and_disp_ly'])
df_outout_input['dollars_w_tpr_ly'] = np.where((df_outout_input['dollars_w_tpr_ly'] == '0') & (df_outout_input['Dollars w/TPR'] != '0'), df_outout_input['Dollars w/TPR'], df_outout_input['dollars_w_tpr_ly'])
df_outout_input['units_w_ftr_wo_disp_ly'] = np.where((df_outout_input['units_w_ftr_wo_disp_ly'] == '0') & (df_outout_input['Units w/Ftr w/o Disp'] != '0'), df_outout_input['Units w/Ftr w/o Disp'], df_outout_input['units_w_ftr_wo_disp_ly'])

df_outout_input['units_w_disp_wo_ftr_ly'] = np.where((df_outout_input['units_w_disp_wo_ftr_ly'] == '0') & (df_outout_input['Units w/Disp w/o Ftr'] != '0'), df_outout_input['Units w/Disp w/o Ftr'], df_outout_input['units_w_disp_wo_ftr_ly'])
df_outout_input['units_w_ftr_and_disp_ly'] = np.where((df_outout_input['units_w_ftr_and_disp_ly'] == '0') & (df_outout_input['Units w/Ftr  Disp'] != '0'), df_outout_input['Units w/Ftr  Disp'], df_outout_input['units_w_ftr_and_disp_ly'])
df_outout_input['units_w_tpr_ly'] = np.where((df_outout_input['units_w_tpr_ly'] == '0') & (df_outout_input['Units w/TPR'] != '0'), df_outout_input['Units w/TPR'], df_outout_input['units_w_tpr_ly'])
df_outout_input['cumulative_distribution_pts_ly'] = np.where((df_outout_input['cumulative_distribution_pts_ly'] == '0') & (df_outout_input['Cumulative Distribution Pts'] != '0'), df_outout_input['Cumulative Distribution Pts'], df_outout_input['cumulative_distribution_pts_ly'])
df_outout_input['avg_no_of_items_ly'] = np.where((df_outout_input['avg_no_of_items_ly'] == '0') & (df_outout_input['Avg # of Items'] != '0'), df_outout_input['Avg # of Items'], df_outout_input['avg_no_of_items_ly'])
df_outout_input['dollars_w_any_promo_ly'] = np.where((df_outout_input['dollars_w_any_promo_ly'] == '0') & (df_outout_input['Dollars w/Any Promo'] != '0'), df_outout_input['Dollars w/Any Promo'], df_outout_input['dollars_w_any_promo_ly'])
df_outout_input['dollars_w_no_promo_ly'] = np.where((df_outout_input['dollars_w_no_promo_ly'] == '0') & (df_outout_input['Dollars w/No Promo'] != '0'), df_outout_input['Dollars w/No Promo'], df_outout_input['dollars_w_no_promo_ly'])
df_outout_input['units_w_any_promo_ly'] = np.where((df_outout_input['units_w_any_promo_ly'] == '0') & (df_outout_input['Units w/Any Promo'] != '0'), df_outout_input['Units w/Any Promo'], df_outout_input['units_w_any_promo_ly'])
df_outout_input['units_w_no_promo_ly'] = np.where((df_outout_input['units_w_no_promo_ly'] == '0') & (df_outout_input['Units w/No Promo'] != '0'), df_outout_input['Units w/No Promo'], df_outout_input['units_w_no_promo_ly'])

#Getting the list of output data columns 
output_col = list(df_output.columns)
output_col.remove('last_year_month')


#Select only necessary dimension and measures from both data set. 
df_outout_input = df_outout_input[output_col]
df_outout_input.to_csv(r'C:\EDC\Other\cruxAssignment\outputFiles\output_transform.csv', index=False)
#print(df_outout_input.head)
