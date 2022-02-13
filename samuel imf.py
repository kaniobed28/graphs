#!/usr/bin/env python
# coding: utf-8

# In[93]:


"October"

import numpy as np
import pandas as pd
import glob
import os
import matplotlib
import matplotlib.pyplot as plt
import datetime
import fnmatch
from matplotlib import dates
import matplotlib
font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 24}

matplotlib.rc('font', **font)
# matplotlib.rc('font'=  serif='cm10', weight ='bold',size="30")
matplotlib.rcParams["savefig.bbox"]  ="tight"
matplotlib.rcParams["figure.titlesize"]  =24
matplotlib.rcParams["figure.titleweight"]  ="bold"
matplotlib.rc('text', usetex=True)
matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']
matplotlib.rcParams['axes.linewidth'] = 2 
matplotlib.rcParams['xtick.major.width'] = 3
matplotlib.rcParams['axes.linewidth'] = 2 
matplotlib.rcParams['xtick.major.width'] = 3
matplotlib.rcParams['ytick.major.width'] = 4
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams["ytick.major.size"] = 9
matplotlib.rcParams.update({'legend.fontsize':22})

#header=gdfheaderfile.readlines()



g2_header =['Year',
 'Day',
 'Hour',
 'Minute',
 'Field_magnitude_average','BZ,nT(GSM)',
 'Speed,km/s',
 'Proton Density',
'Electricfield,mV',
 'SYM/H']


navalues =[9999,99999,999.9, 999999.99,99999.9,999999.99, 
           99.99,99999.99,999.99,99999.99, 99.99000,999999.99,999999.99,99999.99]


# In[27]:


low_res_header = ['YEAR', 'DOY','Hour','Scalar_B','Proton_Density N/cm^3','Kp_index',"Dst_index, nT","F10.7_index"]

gdf = pd.read_csv(r"C:\Users\simba\Downloads\samuel\solargeomag_2018_2.txt" , delim_whitespace=True, skiprows=13, names =low_res_header, na_values =navalues)
gdf


# In[28]:


index = pd.to_datetime(gdf["YEAR"] * 100000 + gdf["DOY"] * 100 + gdf["Hour"],
                       format="%Y%j%H") #Convert YEAR< DOY and HOUR to Datetime Correctly

gdf.set_index(index, inplace =True)
gdf["2018-03":"2018-06"]
gdf["UT"]=gdf.index
gdf


# In[86]:


gdf.plot(y=['Proton_Density N/cm^3','Kp_index',"Dst_index, nT","F10.7_index"],  figsize=(10,10))


# In[79]:


g2_header =['Year',
 'Day',
 'Hour',
 'Minute',
 'Field_magnitude_average','BZ,nT(GSM)',
 'Speed,km/s',
 'Proton Density',
'Electricfield,mV',
 'SYM/H']
gdf2= pd.read_csv(r"C:\Users\simba\Downloads\samuel\Solargeomag_2018.txt" , sep ='\s+', 
                  names = g2_header, na_values =['9999', '99999.9', '*9999*.99',
                                                 '99999','999.99','99999', '99.99000'], skiprows=15, 
                  parse_dates= {"UT" : ["Year","Day","Hour","Minute"]}, keep_date_col=True )
gdf2["UT"] = pd.to_datetime(gdf2.UT, format ="%Y %j %H %M")

gdf2.set_index(gdf2["UT"], inplace=True, drop= True)
gdf2["Time"] = (gdf2['Hour'].astype(str) + '.' + gdf2['Minute'].astype(str))
gdf2["Time"] =pd.to_numeric(gdf2["Time"])
gdf2.set_index("UT", inplace =True,drop=True)
gdf2.head()


# In[80]:


gdf = pd.read_csv(r"C:\Users\simba\Downloads\samuel\solargeomag_2018_2.txt" , sep ='\s+', skiprows=13, names =low_res_header, na_values =navalues)

index = pd.to_datetime(gdf["YEAR"] * 100000 + gdf["DOY"] * 100 + gdf["Hour"], format="%Y%j%H") #Convert YEAR< DOY and HOUR to Datetime Correctly

gdf.set_index(index, inplace =True)
gdf


# In[75]:


gdf2.columns


# In[68]:


fig, axs = plt.subplots(len(gdf.columns), 1, figsize=(25, 28), facecolor='w', edgecolor='k')

fig.subplots_adjust(hspace = 0.3, wspace=0.05)
axs = axs.ravel()
for col in gdf:
    axs[i].plot(gdf.col)


# In[83]:



gdf[["Minute", 'Field_magnitude_average',
       'BZ,nT(GSM)', 'Speed,km/s', 'Proton Density', 'Electricfield,mV',
       'SYM/H', 'Time']]= gdf2[["Minute", 'Field_magnitude_average',
       'BZ,nT(GSM)', 'Speed,km/s', 'Proton Density', 'Electricfield,mV',
       'SYM/H', 'Time']]  #Copy columns from one dataframe to another using the index


# In[ ]:


"Create subplots"
from matplotlib import pyplot as plt
from matplotlib import dates
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
mon1=1

mon2=12
day1=1
day2=31
year=2018

# salu= salu[(salu.UT<9)| (salu.UT>21) ] 
months = dates.MonthLocator()
monthsFmt = dates.DateFormatter('%b')
h_fmt = dates.DateFormatter('%H')
days = dates.DayLocator(interval=10)
dfmt = dates.DateFormatter('%d')
hours =dates.HourLocator(byhour=range(0,24,6))    
mins = dates.MinuteLocator(byminute=None, interval=30)

fig, axs = plt.subplots(5, 1, figsize=(25, 20), facecolor='w', edgecolor='k')

fig.subplots_adjust(hspace = 0.3, wspace=0.05)
axs = axs.ravel()
for i in range(5):
   
    axs[i].set_xlim([datetime.datetime(year, mon1,day1 ,0,0), datetime.datetime(2018, mon2, day2,23,59)])

    axs[i].xaxis.set_major_locator(months)
    axs[i].xaxis.set_major_formatter(monthsFmt)
    axs[i].xaxis.set_minor_locator(days)
    axs[i].grid(b=True, which='major', axis='x',linewidth = 1.5, color='black')
    axs[i].grid(b=True, which='major', axis='y',linestyle ='--',linewidth = 1, color='black')
    axs[i].grid(b=True, which='minor', axis='both',linestyle ='--', linewidth = 1, color='black')
    axs[2].set_ylabel("$Sym/H(nT)$", size=26, weight ='bold')
    axs[0].plot(gdf['Speed,km/s'],lw=2)
    axs[1].plot(gdf['Scalar_B'],lw=2)
    axs[2].plot(gdf2['SYM/H'],lw=2)
    axs[3].plot(gdf['Kp_index'],lw=2)
    axs[4].bar(gdf.index, gdf['F10.7_index'],lw=2, color="k",width =0.1)
fig.align_ylabels()
plt.savefig(str(year)+"imf.png", dpi=500)   


# In[96]:


gdf.columns

