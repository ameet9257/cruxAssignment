#Updated code : 16th April 2022

from unittest import result
import numpy as np
import pandas as pd
from datetime import datetime

#read csv input data to data frame as string
df_input1 = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\input.csv",dtype=str)
df_input2 = pd.read_csv("C:\EDC\Other\cruxAssignment\inputFiles\input.csv",dtype=str)

#Removing the 'W/E '  string from the date field for converting the field into valid date for the joining.
df_input1['PER'] = df_input1['PER'].str.replace('W/E ', '')
df_input1['PER'] = pd.to_datetime(df_input1['PER'])

df_input2['PER'] = df_input2['PER'].str.replace('W/E ', '')
df_input2['PER'] = pd.to_datetime(df_input2['PER'])

#extracting month and year data and adding to the new dataframe 
df_input1["per_year_month_input1"]=(pd.to_datetime(df_input1['PER']).dt.year-1).astype(str)+"-"+df_input1['PER'].dt.month.astype(str)
df_input2["per_year_month_input2"]=(pd.to_datetime(df_input2['PER']).dt.year).astype(str)+"-"+df_input2['PER'].dt.month.astype(str)

#Joining output dataframe with input dataframe based on the ke columns
df_outout_input = df_input1.merge(df_input2, 
                    left_on=['MKT','PROD','CP-CATEGORY','CP-MANUFACTURER','CP-FRANCHISE','CP-BRAND','CP-SUBBRAND','CP-SUBBRAND VARIANT','CP-PRICE TIER','CP-SEGMENT',
                    'per_year_month_input1','PRODUCT CODE'],
                    right_on=['MKT','PROD','CP-CATEGORY','CP-MANUFACTURER','CP-FRANCHISE','CP-BRAND','CP-SUBBRAND','CP-SUBBRAND VARIANT','CP-PRICE TIER','CP-SEGMENT',
                    'per_year_month_input2','PRODUCT CODE'],
                    how='left',suffixes=('_left','_right')
)

# creating the field name mappings between the input and output file
# This will be used to rename the fields name in the output file
dict_col_mapping = {
'MKT'	:	'market',
'PROD'	:	'product',
'CP-CATEGORY'	:	'category',
'CP-MANUFACTURER'	:	'manufacturer',
'CP-FRANCHISE'	:	'franchise',
'CP-BRAND'	:		'brand',
'CP-SUBBRAND'	:	'subbrand',
'CP-SUBBRAND VARIANT'	: 'subbrand_variant',
'CP-PRICE TIER'	:	'pricetier',
'CP-SEGMENT'	:	'segment',
'PER_left'	:	'the_date',
'Dollars_left'	:	'dollars',
'Dollars_right'	:	'dollars_ly',
'Baseline $_left' : 'dollar_baseline',
'Baseline $_right': 'dollar_baseline_ly',
'Units_left'	:	'units',
'Units_right'	:	'units_ly',
'Baseline Units_left' : 'units_baseline',
'Baseline Units_right' : 'units_baseline_ly',
'Dollars w/Ftr w/o Disp_left' : 'dollars_w_ftr_wo_disp',
'Dollars w/Ftr w/o Disp_right' : 'dollars_w_ftr_wo_disp_ly',
'Dollars w/Disp w/o Ftr_left' : 'dollars_w_disp_wo_ftr',
'Dollars w/Disp w/o Ftr_right' : 'dollars_w_disp_wo_ftr_ly',
'Dollars w/Ftr  Disp_left'	: 'dollars_w_ftr_and_disp',
'Dollars w/Ftr  Disp_right'	: 'dollars_w_ftr_and_disp_ly',
'Dollars w/TPR_left'		:	'dollars_w_tpr',
'Dollars w/TPR_right'		:	'dollars_w_tpr_ly',
'Units w/Ftr w/o Disp_left'	:	'units_w_ftr_wo_disp',
'Units w/Ftr w/o Disp_right' : 'units_w_ftr_wo_disp_ly',
'Units w/Disp w/o Ftr_left'	:	'units_w_disp_wo_ftr',
'Units w/Disp w/o Ftr_right' : 'units_w_disp_wo_ftr_ly',
'Units w/Ftr  Disp_left'	:	'units_w_ftr_and_disp',
'Units w/Ftr  Disp_right'		:	'units_w_ftr_and_disp_ly',
'Units w/TPR_left'			:	'units_w_tpr',
'Units w/TPR_right'			:	'units_w_tpr_ly',
'%ACV (% STORES SELLING)_left'	:	'acr',
'Cumulative Distribution Pts_left'	: 'cumulative_distribution_pts',
'Cumulative Distribution Pts_right' : 'cumulative_distribution_pts_ly',
'Avg # of Items_left' : 'avg_no_of_items',
'Avg # of Items_right' : 'avg_no_of_items_ly',
'Dollars w/Any Promo_left' : 'dollars_w_any_promo',
'Dollars w/Any Promo_right' : 'dollars_w_any_promo_ly',
'Dollars w/No Promo_left' : 'dollars_w_no_promo',
'Dollars w/No Promo_right' : 'dollars_w_no_promo_ly',
'Units w/Any Promo_left': 'units_w_any_promo',
'Units w/Any Promo_right': 'units_w_any_promo_ly',
'Units w/No Promo_left' : 'units_w_no_promo',
'Units w/No Promo_right' : 'units_w_no_promo_ly',
'EQ Units_left' : 'eq_units',
'EQ Units_right' : 'eq_units_ly'
}

#renaming the fields
df_outout_input = df_outout_input.rename(columns=dict_col_mapping)

#Select only necessary dimension and measures from both data set. 
df_outout_input = df_outout_input[list(dict_col_mapping.values())]

#adding some extra measures and dimensions to the data frame
df_outout_input = df_outout_input.assign(at3 = '', mt1 = 0 , mt2 = 0, mt3=0)

#loading the transfrom data into csv file.
df_outout_input.to_csv(r'C:\EDC\Other\cruxAssignment\outputFiles\output_transform.csv', index=False)
