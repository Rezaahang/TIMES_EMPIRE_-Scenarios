# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:37:28 2021

@author: mohaa
"""

import pandas as pd
import numpy as np
import csv

#### Reading the already exist stochastic scenarios to underestand the structure ####
Stochastic_ElectricLoadRaw = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/3sce from TF/Stochastic_ElectricLoadRaw.tab',delimiter='\t')
Stochastic_HydroGenMaxSeasonalProduction = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/3sce from TF/Stochastic_HydroGenMaxSeasonalProduction.tab',delimiter='\t')
Stochastic_StochasticAvailability = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/3sce from TF/Stochastic_StochasticAvailability.tab',delimiter='\t')

elc_load = Stochastic_ElectricLoadRaw.copy()
hydro_max = Stochastic_HydroGenMaxSeasonalProduction.copy()
sto_avai = Stochastic_StochasticAvailability.copy()


##### Generating a dict to convert countries' name abbreviations to real name####

# f= elc_load.loc[:,'Node'].value_counts()
# h = pd.Series(f,name='vals')
# h=h.to_frame()
# h['name']=h.index
# abb = ['DK','BA','GB', 'FR', 'EE', 'SI', 'AT', 'CH', 'NL', 'RO', 'HR', 'LV', 'LT', 'LU', 'SE', 'PL', 'DE', 'BE', 'NO2', 'GR', 'BG', 'MK', 'SK', 'IE', 'RS', 'NO1', 'IT', 'FI', 'HU', 'ES', 'NO3', 'NO4', 'CZ', 'PT', 'NO5']
# # abb =  ['LT','SE', 'CZ', 'SI', 'SK', 'NO4', 'HR', 'EE', , 'NL', 'HU', 'BG', 'PT', 'RS', 'LV', 'NO5', 'NO1', 'CH', 'FR', , 'MK', 'NO2', 'AT', 'FI', 'GB', 'BE', 'GR', 'IT', 'RO', 'LU', 'IE', 'DE', 'PL', 'ES', 'NO3']
# h['abb'] = abb
# name_countries = dict(zip(h.abb, h.name))


name_countries = {'DK': 'Denmark','BA':'BosniaH','GB':'GreatBrit.', 'FR':'France', 'EE':'Estonia', 'SI':'Slovenia', 'AT':'Austria', 'CH':'Switzerland', 'NL':'Netherlands', 'RO':'Romania', 'HR':'Croatia', 'LV':'Latvia', 'LT':'Lithuania', 'LU':'Luxemb.', 'SE':'Sweden', 'PL':'Poland', 'DE':'Germany', 'BE':'Belgium', 'NO2':'NO2', 'GR':'Greece', 'BG':'Bulgaria', 'MK':'Macedonia', 'SK':'Slovakia', 'IE':'Ireland', 'RS':'Serbia', 'NO1':'NO1', 'IT':'Italy', 'FI':'Finland', 'HU':'Hungary', 'ES':'Spain', 'NO3':'NO3', 'NO4':'NO4', 'CZ':'CzechR', 'PT':'Portugal', 'NO5':'NO5'}


###### Generating elc_load with value zero to fill with new data from our scenarios ######
elc_load.columns
Col = ['ElectricLoadRaw_in_MW']
elc_load_dict = {}
period = [0,1,2,3,4,5,6,7]
scenario = ['scenario1', 'scenario2', 'scenario3']

for i in period:
    for it in scenario:
        for item in name_countries.items():
            elc_load_dict['elc_load_period' + str(i+1) + '_' + item[1] +  '_' + str(it)] = elc_load[(elc_load['Period'] == i+1) & (elc_load['Node'] == item[1]) & (elc_load['Scenario'] == it)]



#### Importing generated scenarios file ######
season = ['winter', 'spring', 'summer', 'autumn']
elc_new_dict = {}

for i in period:
    if i+1 == 1:
        for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Electricload_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea +'_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
    if i+1 == 2:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Electricload_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
    if i+1 == 3:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Electricload_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
    if i+1 == 4:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Electricload_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
                    
    if i+1 == 5:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Electricload_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
                    
    if i+1 == 6:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Electricload_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
                    
                    
    if i+1 == 7:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Electricload_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
    if i+1 == 8:
       for s in season:
            for sea in scenario:
                
                elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Electricload_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[0:168]
                    
                elif sea == 'scenario2':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[168:336]
                    
                elif sea == 'scenario3':
                    elc_new_dict['elc_period'+ str(i+1)+ '_' + sea + '_'+ s] =  elc.iloc[336:504]
                    
                    

for s in season:
    for keys in elc_new_dict:
        if s in keys:
            if s == 'winter':
                elc_new_dict[keys]['Operationalhour'] = range(1,169)
    
            if s == 'spring':
                elc_new_dict[keys]['Operationalhour'] = range(169,337)
                
            if s == 'summer':
                elc_new_dict[keys]['Operationalhour'] = range(337,505)
                
            if s == 'autumn':
                elc_new_dict[keys]['Operationalhour'] = range(505,673) 
                
        else:
            pass


# for i in elc_new_dict:
#     if 'period1' in i:
#         if 'scenario1' in i:
#             i
#     elif: 'period2' in i:
#     elif: 'period3' in i:
#     elif: 'period4' in i:
#     elif: 'period5' in i:
#     elif: 'period6' in i:
#     elif: 'period7' in i:
#     elif: 'period8' in i:




# def finder_new(period, country, season, scenario):
#     for item in elc_new_dict:
#         if period in item: 
#             if season in item:
#                 if scenario in item:
#                     for name in name_countries:
#                         if name_countries[name] == country:
#                             x = elc_new_dict[item].loc[:, (name,'Operationalhour')]
#         else:
#             pass
#     return x

# def finder(period, country, season, scenario):
#     for item in elc_load_dict:
#         if period in item: 
#             if season in item:
#                 if scenario in item:
#                     if country in item:
#                         elc_load_dict[item]['ElectricLoadRaw_in_MW'] = 0
#                         c = elc_load_dict[item]['Operationalhour']
#                         for i in c:
#                             for k in finder_new(period, country, season, scenario)['Operationalhour']:
#                                 if i == k:
#                                     elc_load_dict[item]['New_ElectricLoadRaw_in_MW']= finder_new(period, country, season, scenario)[name]
                        
#         else:
#             pass
#     return x



##https://www.delftstack.com/howto/python-pandas/pandas-replace-values-in-column/
      
                        
# re = elc_new_dict['elc_period1_scenario1_autumn'].copy()
# re1 = elc_load_dict['elc_load_period1_Austria_scenario1'].copy()    

# #df.loc[df['column_name'] == some_value]

# re1['ElectricLoadRaw_in_MW']= 0 
##https://stackoverflow.com/questions/36684013/extract-column-value-based-on-another-column-pandas-dataframe


# for i in re['Operationalhour']:
#     for it in re1['Operationalhour']:
#         if i == it:
#             a = re.loc[re['Operationalhour'] == i, 'AT' ]
#             b = re1.loc[re1['Operationalhour'] == i, 'ElectricLoadRaw_in_MW' ]
#             re1['ElectricLoadRaw_in_MW'] = re1['ElectricLoadRaw_in_MW'].map({b:a})
            
Origin_elc = elc_load.copy()
new_elc = elc_new_dict.copy()

Origin_elc['new_index']=Origin_elc['Node']

for i in name_countries:
    for it in Origin_elc['new_index']:    
        if name_countries[i] == it:
            Origin_elc.loc[Origin_elc.new_index == it, 'new_index' ] = i 
            
# Origin_elc.to_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/Origin_elc.csv', index = False)
Ori_elc = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/Origin_elc.csv')
# Ori_elc['new_index']
# Ori_elc = Origin_elc.copy() 
Ori_elc['index'] =  Ori_elc['new_index'] + '_' + Ori_elc['Operationalhour'].astype(str) + '_' + Ori_elc['Period'].astype(str) +  '_' + Ori_elc['Scenario'] 
origin = Ori_elc.set_index('index') 

#############
sep_data = {}

for i in elc_new_dict:
    for it in name_countries:
        sep_data[i+'_'+it] = elc_new_dict[i].loc[:,(it,'time','hour','month','Operationalhour' )]    

for i in sep_data:
    sep_data[i]['new_index'] = sep_data[i].columns[0] + '_' + sep_data[i]['Operationalhour'].astype(str) 

for i in sep_data:
    if 'period1' in i:
        sep_data[i]['Period'] = 1 
    elif 'period2' in i:
        sep_data[i]['Period'] = 2 
    elif 'period3' in i:
        sep_data[i]['Period'] = 3
    elif 'period4' in i:
        sep_data[i]['Period'] = 4 
    elif 'period5' in i:
        sep_data[i]['Period'] = 5 
    elif 'period6' in i:
        sep_data[i]['Period'] = 6 
    elif 'period7' in i:
        sep_data[i]['Period'] = 7 
    elif 'period8' in i:   
        sep_data[i]['Period'] = 8 
        

for i in sep_data:
    if 'scenario1' in i:
        sep_data[i]['Scenario'] = 1 
    elif 'scenario2' in i:
        sep_data[i]['Scenario'] = 2 
    elif 'scenario3' in i:
        sep_data[i]['Scenario'] = 3
        
        
        


for i in sep_data:
    sep_data[i]['new'] = sep_data[i]['new_index'] + '_' + sep_data[i]['Period'].astype(str) + '_' + 'scenario'+ sep_data[i]['Scenario'].astype(str)  


New = {}
for i in sep_data:
    New[i] = sep_data[i].set_index('new')
    


# f = sep_data['elc_period1_scenario2_spring_NL'].columns[0]



#https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html#:~:text=Combine%20data%20from%20multiple%20files,common%20fields%20(join%20keys).

#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

for i in New:
    New[i].columns = ['Nod','time','hour','month','Operationalhour','new_index', 'Period', 'Scenario']
    


New_list = []
for i in New:
    New_list.append(New[i])

New_shape = pd.concat(New_list)

new_shape = New_shape.loc[:,'Nod']
origin['new_value']= 0
origin['new_value'] = new_shape


boolian_nan = pd.isnull(origin['new_value'])

aa = origin[boolian_nan].loc[:,('new_value','ElectricLoadRaw_in_MW')]
aa['new_value'] = aa['ElectricLoadRaw_in_MW']
enter = aa['new_value']
ori = origin.copy()
ori['new_value'] = ori['new_value'].fillna(0)



# https://stackoverflow.com/questions/39903090/efficiently-replace-values-from-a-column-to-another-column-pandas-dataframe

ori['new_value'] = np.where(ori['new_value'] == 0, ori['ElectricLoadRaw_in_MW'], ori['new_value'])

ori['ElectricLoadRaw_in_MW'] = ori['new_value']

ori.drop(['new_index', 'new_value'], inplace=True, axis=1)
# ori['new_value'] = aa['new_value']

ori.reset_index(inplace = True, drop = True)

# booli = pd.isnull(ori['ElectricLoadRaw_in_MW'])

# aaa = ori[booli].loc[:,'ElectricLoadRaw_in_MW']


ori.to_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/New_scenarios_Tabfile' + "/Stochastic_ElectricLoadRaw" + '.tab',header=True, index=None, sep='\t', mode='w')

#####
#####
#####



################## HydroGenMaxSeasonalProduction#####################


#######
#######
#######

hydro_dict = {}


for i in period:
    if i+1 == 1:
        for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Hydroseasonal_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea +'_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
    if i+1 == 2:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Hydroseasonal_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
    if i+1 == 3:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Hydroseasonal_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
    if i+1 == 4:
       for s in season:
            for sea in scenario:
            
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Hydroseasonal_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
                    
    if i+1 == 5:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Hydroseasonal_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
                    
    if i+1 == 6:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Hydroseasonal_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
                    
                    
    if i+1 == 7:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Hydroseasonal_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
    if i+1 == 8:
       for s in season:
            for sea in scenario:
                
                hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Hydroseasonal_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[0:168]
                    
                elif sea == 'scenario2':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[168:336]
                    
                elif sea == 'scenario3':
                    hydro_dict['hydro_period'+ str(i+1)+ '_' + sea + '_'+ s] =  hydro.iloc[336:504]
                    
                    

for s in season:
    for keys in hydro_dict:
        if s in keys:
            if s == 'winter':
                hydro_dict[keys]['Operationalhour'] = range(1,169)
    
            if s == 'spring':
                hydro_dict[keys]['Operationalhour'] = range(169,337)
                
            if s == 'summer':
                hydro_dict[keys]['Operationalhour'] = range(337,505)
                
            if s == 'autumn':
                hydro_dict[keys]['Operationalhour'] = range(505,673) 
                
        else:
            pass


Origin_hydro = hydro_max.copy()
# new_elc = elc_new_dict.copy()

Origin_hydro['new_index']=Origin_hydro['Node']

for i in name_countries:
    for it in Origin_hydro['new_index']:    
        if name_countries[i] == it:
            Origin_hydro.loc[Origin_hydro.new_index == it, 'new_index' ] = i 
            
#Origin_hydro.to_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/Origin_hydro.csv', index = False)
#Ori_hydro = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/Origin_hydro.csv')
# Ori_elc['new_index']
Ori_hydro = Origin_hydro.copy() 
Ori_hydro['index'] =  Ori_hydro['new_index'] + '_' + Ori_hydro['Operationalhour'].astype(str) + '_' + Ori_hydro['Period'].astype(str) +  '_' + Ori_hydro['Scenario'] 
origin_hydro = Ori_hydro.set_index('index') 


sep_data_hydro = {}

for i in hydro_dict:
    for it in name_countries:
        if it in hydro_dict[i].columns.tolist():
            sep_data_hydro[i+'_'+it] =hydro_dict[i].loc[:,(it,'time','Operationalhour')]
        else:
            pass

        

for i in sep_data_hydro:
    sep_data_hydro[i]['new_index'] = sep_data_hydro[i].columns[0] + '_' + sep_data_hydro[i]['Operationalhour'].astype(str) 

for i in sep_data_hydro:
    if 'period1' in i:
        sep_data_hydro[i]['Period'] = 1 
    elif 'period2' in i:
        sep_data_hydro[i]['Period'] = 2 
    elif 'period3' in i:
        sep_data_hydro[i]['Period'] = 3
    elif 'period4' in i:
        sep_data_hydro[i]['Period'] = 4 
    elif 'period5' in i:
        sep_data_hydro[i]['Period'] = 5 
    elif 'period6' in i:
        sep_data_hydro[i]['Period'] = 6 
    elif 'period7' in i:
        sep_data_hydro[i]['Period'] = 7 
    elif 'period8' in i:   
        sep_data_hydro[i]['Period'] = 8 
        

for i in sep_data_hydro:
    if 'scenario1' in i:
        sep_data_hydro[i]['Scenario'] = 1 
    elif 'scenario2' in i:
        sep_data_hydro[i]['Scenario'] = 2 
    elif 'scenario3' in i:
        sep_data_hydro[i]['Scenario'] = 3
        
        
        


for i in sep_data_hydro:
    sep_data_hydro[i]['new'] = sep_data_hydro[i]['new_index'] + '_' + sep_data_hydro[i]['Period'].astype(str) + '_' + 'scenario'+ sep_data_hydro[i]['Scenario'].astype(str)  


New_hydro = {}
for i in sep_data_hydro:
    New_hydro[i] = sep_data_hydro[i].set_index('new')
    


# f = sep_data['elc_period1_scenario2_spring_NL'].columns[0]



#https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html#:~:text=Combine%20data%20from%20multiple%20files,common%20fields%20(join%20keys).

#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

for i in New_hydro:
    New_hydro[i].columns = ['Nod','time','Operationalhour','new_index', 'Period', 'Scenario']
    


New_list_hydro = []
for i in New_hydro:
    New_list_hydro.append(New_hydro[i])

New_shape_hydro = pd.concat(New_list_hydro)

new_shape_hydro = New_shape_hydro.loc[:,'Nod']
origin_hydro['new_value']= 0
origin_hydro['new_value'] = new_shape_hydro



bool_nan = pd.isnull(origin_hydro['new_value'])

aaa = origin_hydro[bool_nan].loc[:,('new_value','HydroGeneratorMaxSeasonalProduction')]
aaa['new_value'] = aaa['HydroGeneratorMaxSeasonalProduction']
enter_hydro = aaa['new_value']
ori_hydro = origin_hydro.copy()
# ori_hydro['new_value'] = ori_hydro['new_value'].fillna(0)
ori_hydro['new_value'] = ori_hydro['new_value'].replace(np.nan, 1.99)



# https://stackoverflow.com/questions/39903090/efficiently-replace-values-from-a-column-to-another-column-pandas-dataframe

ori_hydro['new_value'] = np.where(ori_hydro['new_value'] == 1.99 , ori_hydro['HydroGeneratorMaxSeasonalProduction'], ori_hydro['new_value'])

ori_hydro['HydroGeneratorMaxSeasonalProduction'] = ori_hydro['new_value']

ori_hydro.drop(['new_index', 'new_value'], inplace=True, axis=1)
# ori['new_value'] = aa['new_value']

ori_hydro.reset_index(inplace = True, drop = True)

# booli = pd.isnull(ori['ElectricLoadRaw_in_MW'])

# aaa = ori[booli].loc[:,'ElectricLoadRaw_in_MW']



ori_hydro.to_csv(
        r'C:/Users/mohaa/Desktop/Sto. Sce/New_scenarios_Tabfile' + "/Stochastic_HydroGenMaxSeasonalProduction" + '.tab',
        header=True, index=None, sep='\t', mode='w')








#####
#####
#####



################## StochasticAvailability#####################


#######
#######
#######

print(sto_avai.head())
sto_avai['IntermitentGenerators'].value_counts()

sto_dict = {}


for i in period:
    if i+1 == 1:
        for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Hydroror_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/solar_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Windoffshore_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Windonshore_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
    if i+1 == 2:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Hydroror_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/solar_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Windoffshore_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 1/Windonshore_EMPIRE_3scen_weekly_1_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
    if i+1 == 3:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Hydroror_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/solar_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Windoffshore_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Windonshore_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
    if i+1 == 4:
       for s in season:
            for sea in scenario:
            
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Hydroror_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/solar_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Windoffshore_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 2/Windonshore_EMPIRE_3scen_weekly_2_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
                    
    if i+1 == 5:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Hydroror_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/solar_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Windoffshore_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Windonshore_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
                    
    if i+1 == 6:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Hydroror_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/solar_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Windoffshore_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 3/Windonshore_EMPIRE_3scen_weekly_3_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
                    
                    
    if i+1 == 7:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Hydroror_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/solar_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Windoffshore_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Windonshore_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                
                   
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
    if i+1 == 8:
       for s in season:
            for sea in scenario:
                
                sto_ror = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Hydroror_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_sol = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/solar_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_off = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Windoffshore_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                sto_on = pd.read_csv(r'C:/Users/mohaa/Desktop/Sto. Sce/period 4/Windonshore_EMPIRE_3scen_weekly_4_'+ s +'.csv')
                
                if sea == 'scenario1':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[0:168]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[0:168]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[0:168]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[0:168]
                    
                elif sea == 'scenario2':
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[168:336]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[168:336]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[168:336]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[168:336]
                    
                    
                elif sea == 'scenario3':
                    
                    sto_dict['sto_ror_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_ror.iloc[336:504]
                    sto_dict['sto_sol_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_sol.iloc[336:504]
                    sto_dict['sto_off_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_off.iloc[336:504]
                    sto_dict['sto_on_period'+ str(i+1)+ '_' + sea +'_'+ s] =  sto_on.iloc[336:504]
                    
                    

for s in season:
    for keys in sto_dict:
        if s in keys:
            if s == 'winter':
                sto_dict[keys]['Operationalhour'] = range(1,169)
    
            if s == 'spring':
                sto_dict[keys]['Operationalhour'] = range(169,337)
                
            if s == 'summer':
                sto_dict[keys]['Operationalhour'] = range(337,505)
                
            if s == 'autumn':
                sto_dict[keys]['Operationalhour'] = range(505,673) 
                
        else:
            pass


Origin_sto = sto_avai.copy()
# new_elc = elc_new_dict.copy()
Origin_sto.head()
Origin_sto['new_index']=Origin_sto['Node']

for i in name_countries:    
    Origin_sto['new_index'].replace(name_countries[i], i, inplace=True)



Ori_sto = Origin_sto.copy() 
Ori_sto['index'] =  Ori_sto['new_index'] + '_' + Ori_sto['Operationalhour'].astype(str) + '_' + Ori_sto['IntermitentGenerators'] + '_' + Ori_sto['Period'].astype(str) +  '_' + Ori_sto['Scenario'] 
origin_sto = Ori_sto.set_index('index') 
Ori_sto['index'].head()

sep_data_sto = {}

for i in sto_dict:
    for it in name_countries:
        if it in sto_dict[i].columns.tolist():
            sep_data_sto[i+'_'+it] =sto_dict[i].loc[:,(it,'time','Operationalhour')]
        else:
            pass

        

for i in sep_data_sto:
    sep_data_sto[i]['new_index'] = sep_data_sto[i].columns[0] + '_' + sep_data_sto[i]['Operationalhour'].astype(str) 

for i in sep_data_sto:
    if 'period1' in i:
        sep_data_sto[i]['Period'] = 1 
    elif 'period2' in i:
        sep_data_sto[i]['Period'] = 2 
    elif 'period3' in i:
        sep_data_sto[i]['Period'] = 3
    elif 'period4' in i:
        sep_data_sto[i]['Period'] = 4 
    elif 'period5' in i:
        sep_data_sto[i]['Period'] = 5 
    elif 'period6' in i:
        sep_data_sto[i]['Period'] = 6 
    elif 'period7' in i:
        sep_data_sto[i]['Period'] = 7 
    elif 'period8' in i:   
        sep_data_sto[i]['Period'] = 8 
        

for i in sep_data_sto:
    if 'scenario1' in i:
        sep_data_sto[i]['Scenario'] = 1 
    elif 'scenario2' in i:
        sep_data_sto[i]['Scenario'] = 2 
    elif 'scenario3' in i:
        sep_data_sto[i]['Scenario'] = 3

    
for i in sep_data_sto:
    if 'ror' in i: 
        sep_data_sto[i]['process'] = 'Hydrorun-of-the-river'
    if 'sol' in i:
        sep_data_sto[i]['process'] = 'Solar'
    if 'sto_off' in i:
        sep_data_sto[i]['process'] = 'Windoffshore'
    if 'sto_on' in i:
        sep_data_sto[i]['process'] = 'Windonshore'


for i in sep_data_sto:
    sep_data_sto[i]['new'] = sep_data_sto[i]['new_index'] + '_' + sep_data_sto[i]['process'] + '_' + sep_data_sto[i]['Period'].astype(str) + '_' + 'scenario'+ sep_data_sto[i]['Scenario'].astype(str)  


New_sto = {}
for i in sep_data_sto:
    New_sto[i] = sep_data_sto[i].set_index('new')
    


# f = sep_data['elc_period1_scenario2_spring_NL'].columns[0]



#https://datacarpentry.org/python-ecology-lesson/05-merging-data/index.html#:~:text=Combine%20data%20from%20multiple%20files,common%20fields%20(join%20keys).

#https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html

for i in New_sto:
    New_sto[i].columns = ['Nod','time','Operationalhour','new_index', 'Period', 'Scenario', 'process']
    


New_list_sto = []
for i in New_sto:
    New_list_sto.append(New_sto[i])

New_shape_sto = pd.concat(New_list_sto)

new_shape_sto = New_shape_sto.loc[:,'Nod']
origin_sto['new_value']= 1.99
origin_sto['new_value'] = new_shape_sto

origin_sto.columns

boo_nan = pd.isnull(origin_sto['new_value'])

aaaa = origin_sto[boo_nan].loc[:,('new_value','GeneratorStochasticAvailabilityRaw')]
aaaa['new_value'] = aaaa['GeneratorStochasticAvailabilityRaw']
enter_sto = aaaa['new_value']
ori_sto = origin_sto.copy()
# ori_hydro['new_value'] = ori_hydro['new_value'].fillna(0)
ori_sto['new_value'] = ori_sto['new_value'].replace(np.nan, 1.99)



# https://stackoverflow.com/questions/39903090/efficiently-replace-values-from-a-column-to-another-column-pandas-dataframe

ori_sto['new_value'] = np.where(ori_sto['new_value'] == 1.99 , ori_sto['GeneratorStochasticAvailabilityRaw'], ori_sto['new_value'])

ori_sto['GeneratorStochasticAvailabilityRaw'] = ori_sto['new_value']


ori_sto.columns
sto_avai.columns



ori_sto.drop(['new_index', 'new_value'], inplace=True, axis=1)
# ori['new_value'] = aa['new_value']

ori_sto.reset_index(inplace = True, drop = True)

# booli = pd.isnull(ori['ElectricLoadRaw_in_MW'])

# aaa = ori[booli].loc[:,'ElectricLoadRaw_in_MW']


ori_sto.to_csv(
        r'C:/Users/mohaa/Desktop/Sto. Sce/New_scenarios_Tabfile' + "/Stochastic_StochasticAvailability" + '.tab',
        header=True, index=None, sep='\t', mode='w')




