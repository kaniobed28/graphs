import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime
import fnmatch
from matplotlib import dates
import matplotlib
from matplotlib import dates
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
navalues =[9999,99999,999.9, 999999.99,99999.9,999999.99, 
           99.99,99999.99,999.99,99999.99, 99.99000,999999.99,999999.99,99999.99]

low_res_header = ['YEAR', 'DOY','Hour',"Dst_index, nT","F10.7_index"]

# Reading Solargeomag_2018_low.txt as a csv file
gdf = pd.read_csv(r"Solargeomag_2018_low.txt" , delim_whitespace=True, skiprows=13, names =low_res_header, na_values =navalues)
#Convert YEAR< DOY and HOUR to Datetime Correctly
index = pd.to_datetime(gdf["YEAR"] * 100000 + gdf["DOY"] * 100 + gdf["Hour"],
                       ) 

gdf.set_index(index, inplace =True)
gdf["2018-03":"2018-06"]
gdf["UT"]=gdf.index
gdf = pd.read_csv(r"solargeomag_2018_low resolution.txt" , sep ='\s+', skiprows=13, names =low_res_header, na_values =navalues)

index = pd.to_datetime(gdf["YEAR"] * 100000 + gdf["DOY"] * 100 + gdf["Hour"], format="%Y%j%H") #Convert YEAR< DOY and HOUR to Datetime Correctly

gdf.set_index(index, inplace =True)
mon1=1

mon2=12
day1=1
day2=31
year=2018

months = dates.MonthLocator() #The matplotlib.ticker.MultipleLocator class is used for setting a tick for every integer
#  multiple of a base within the view interval
monthsFmt = dates.DateFormatter('%b') #Formatting to month form
h_fmt = dates.DateFormatter('%H')##Formatting to hour form
days = dates.DayLocator(interval=10)
dfmt = dates.DateFormatter('%d') ##Formatting to day form
hours =dates.HourLocator(byhour=range(0,24,6))    
mins = dates.MinuteLocator(byminute=None, interval=30)

fig, axs = plt.subplots(2, 1, figsize=(25, 20), facecolor='w', edgecolor='k')


axs[1].grid(b=True, which='major', axis='x',linewidth = 1.5, color='black')
axs[1].grid(b=True, which='major', axis='y',linestyle ='--',linewidth = 1, color='black')
axs[1].grid(b=True, which='minor', axis='both',linestyle ='--', linewidth = 1, color='black')
axs[0].grid(b=True, which='major', axis='x',linewidth = 1.5, color='black')
axs[0].grid(b=True, which='major', axis='y',linestyle ='--',linewidth = 1, color='black')
axs[0].grid(b=True, which='minor', axis='both',linestyle ='--', linewidth = 1, color='black')


# This section of the code is responsible for setting x-axis label on each graph of respective index
axs[1].xaxis.set_major_locator(months)
axs[0].xaxis.set_major_locator(months)


# This section is used for setting label for the y-axis with font size of 30 and making the font bold.
axs[0].set_ylabel("$Dst(nT)$", size=32, weight ='bold')

axs[1].set_ylabel("$F10.7(SFU)$", size=32, weight ='bold')

# This section of the code is setting range for the y-axis.It takes one argument with a python list of two integers.
axs[0].set_ylim([-200,50])

axs[1].set_ylim([65,90])
x = ["1/12","2/12","3/12","4/12","5/12","6/12","7/12","8/12","9/12","10/12","11/12","12/12"]

x = pd.DataFrame(x,columns=["x"])
# This section of the code is for plot the graph. The bar is responsible for plotting bar graph and the plot method is for
# plotting a linear graph.
axs[0].plot(gdf['Dst_index, nT'],lw=2,color="red")   
axs[1].bar(gdf.index, gdf['F10.7_index'],lw=2,width =0.1,color="blue")

axs[0].set_xticklabels(x["x"],fontsize= 28)
axs[1].set_xticklabels(x["x"],fontsize= 28)

axs[0].set_yticklabels(np.arange(-200,50,50),fontsize= 28)
axs[1].set_yticklabels(np.arange(65,90,5),fontsize= 28)

axs[0].tick_params(labelbottom = False)

fig.text(0.5, 0.04, 'Month', ha='center',size = 32 ,weight = 'bold')# This line of code is for labeling the x-axis 'Month'.
fig.align_ylabels()
# Saving the graph as a png file(picture)
plt.savefig(str(year)+"imf2.jpg", dpi=500)# this line of code is responsible for saving the graph as an image(png file).
plt.show()# this line of code is responsible for showing the plotted graph to the screen.
