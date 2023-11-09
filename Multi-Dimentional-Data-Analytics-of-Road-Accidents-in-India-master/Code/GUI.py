import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import sklearn
import csv
import os
import xlrd
from collections import defaultdict
import math as m
from jupyterthemes import jtplot

def block1():
    df = pd.read_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/roadAccStats13-16.csv')

    mean13 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2013'])
    print("Mean of accidents happened in all states in year 2013: {}".format(mean13))
    mean14 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2014'])
    print("Mean of accidents happened in all states in year 2014 : {}".format(mean14))
    mean15 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2015'])
    print("Mean of accidents happened in all states in year 2015 : {}".format(mean15))
    mean16 = np.mean(df['State/UT-Wise Total Number of Road Accidents during - 2016'])
    print("Mean of accidents happened in all states in 2016 {}".format(mean16))

    labels = 'State/UT-Wise Total Number of Road Accidents during - 2013', 'State/UT-Wise Total Number of Road Accidents during - 2014', 'State/UT-Wise Total Number of Road Accidents during - 2015', 'State/UT-Wise Total Number of Road Accidents during - 2016'
    sizes = [mean13, mean14, mean15, mean16]
    colors = ['gold', 'green', 'blue', 'orange']
    explode = (0.01, 0.01, 0.01, 0.01)
    plt.pie(sizes, labels = labels, colors = colors, explode = explode,
        shadow = True, autopct = '%.4f%%', startangle = 140)
    plt.axis('equal')
    plt.show()

    plt.figure(figsize = (15,5))
    plt.rcParams.update({'font.size':9})
    y = df['State/UT-Wise Total Number of Road Accidents during - 2013']
    yd = df['States/UTs']
    p =df['States/UTs'].nunique()
    d = np.linspace(1,p,p)   # refer notes
    plt.bar(d, y, align = 'center')
    plt.xticks(d, yd, rotation = 90)
    plt.xlabel('States')
    plt.ylabel('Number of Accidents')
    plt.title('Total number of Accidents in each State.')
    plt.show()

def block2():
    df3 = pd.read_excel('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/accidents03-16.xls')
    df8 = pd.DataFrame(columns = ['Year','Count'])
    df8['Year'] = df3[df3['States/Uts'] == 'All India'].columns[1:]
    df8 = df3[df3['States/Uts'] == "All India"]
    df9 = df8.T
    df9.to_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/accidentRate.csv')
    # plt.figure(figsize = (20,10))
    plt.rcParams.update({'font.size' : 18})

    df9.iloc[1:].plot(figsize = (20,10), legend =  False)
    plt.xlabel("Year")
    plt.ylabel("No of Accidents")
    plt.title("No. of Accidents/Year")
    plt.show()

def block3():
    df4 = pd.read_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/laneAccidents.csv')
    df4.dropna(axis = 0, how ='any', inplace = True)
    singleLaneAcc = df4['Single Lane - Accident - 2014 per 1L people']
    twoLaneAcc = df4['Two Lanes - Accident - 2014 per 1L people']
    threeLaneAcc = df4['3 Lanes or more w.o Median - Accident - 2014 per 1L people']
    fourLaneAcc = df4['4 Lanes with Median - Accident - 2014 per 1L people']
    plt.figure(figsize = (20,10))
    plt.rcParams.update({'font.size':18})
    UT = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])

    plt.bar(UT-0.2, singleLaneAcc, label='Single Lane', width = 0.2,
            align = 'center')
    plt.bar(UT, twoLaneAcc, label = 'Two Lane', width = 0.2,
            align = 'center')
    plt.bar(UT+0.2, threeLaneAcc, label = 'Three Lane', width = 0.2,
            align = 'center')
    plt.bar(UT+0.4, fourLaneAcc, label = 'Four Lane', width =0.2,
            align = 'center')

    plt.xticks(UT, df4['State/UT'], rotation = 'vertical' )
    plt.legend(loc = 'best')
    plt.title("Number of ACCIDENTS for 1,2,3,4 LANE per 1L population of resp. state.")
    plt.show()


def block4():
    df = pd.read_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/roadAccStats13-16.csv')
    df5 = pd.read_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/reasonOfAccident.csv')

    driverFault = df5['Fault of Driver-Number of Persons-Killed - 2014 per 1L people']
    otherDriversFault = df5['Fault of Driver of other vehicles-Number of Persons-Killed - 2014 per 1L people']
    pedestrianFault = df5['Fault of Pedestrian-Number of Persons-Killed - 2014 per 1L people']
    conditionOfVehicleFault = df5['Defect in Condition of Motor Vehicle-Number of Persons-Killed - 2014 per 1L people']
    roadConditionFault = df5['Defect in Road Condition-Number of Persons-Killed - 2014 per 1L people']
    weatherConditionFault = df5['Weather Condition-Number of Persons-Killed - 2014 per 1L people']
    passengerFault = df5['Fault of Passenger-Number of Persons-Killed - 2014 per 1L people']
    poorLightFault = df5['Poor light-Number of Persons-Killed - 2014 per 1L people']
    bouldersFault = df5['Falling of boulders-Number of Persons-Killed - 2014 per 1L people']
    otherCauses = df5['Other causes/causes not known-Number of Persons-Killed - 2014 per 1L people']

    plt.figure(figsize=(20,10))
    plt.rcParams.update({'font.size':18})

    UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
    UT=UT*3

    plt.bar(UT-0.6, driverFault, width = 0.2, color = 'r', align = 'center', label = 'Driver')
    plt.bar(UT-0.4, otherDriversFault,width=0.2, color='black', align='center', label='Other driver\'s')
    plt.bar(UT-0.2, pedestrianFault,width=0.2, color='g', align='center', label='Pedestrian')
    plt.bar(UT, conditionOfVehicleFault,width=0.2, color='b', align='center', label='Condition of Vehicle')
    plt.bar(UT+0.2, roadConditionFault,width=0.2, color='yellow', align='center', label='Road Condition')
    plt.bar(UT+0.4, weatherConditionFault,width=0.2, color='brown', align='center', label='Weather Condition')
    plt.bar(UT+0.6, passengerFault,width=0.2, color='purple', align='center', label='Passenger')
    plt.bar(UT+0.8, poorLightFault,width=0.2, color='orange', align='center', label='Poor light')
    plt.bar(UT+1.0, bouldersFault,width=0.2, color='pink', align='center', label='Boulders')
    plt.bar(UT+1.2, otherCauses,width=0.2, color='cyan', align='center', label='Other Causes')

    plt.xticks(UT,df['States/UTs'],rotation='vertical')
    plt.legend(loc='upper left', bbox_to_anchor=(1,1))
    plt.title("Number of people KILLED for each different REASON per 1L population of that state")
    plt.show()


def block5():
    df6 = pd.read_csv('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/typeOfVehicle.csv')
    df6.dropna(axis = 0, how = 'any', inplace = True)
    plt.figure(figsize=(20,10))
    plt.rcParams.update({'font.size':18})
    UT=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
    UT=UT*2

    plt.bar(UT-0.6,df6['Two-Wheelers - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='r',align='center',label='Two-Wheelers')
    plt.bar(UT-0.4,df6['Auto-Rickshaws - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='black',align='center',label='Auto-Rickshaws')
    plt.bar(UT-0.2,df6['Cars, Jeeps,Taxis - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='g',align='center',label='Cars,Jeeps,Taxis')
    plt.bar(UT,df6['Buses - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='b',align='center',label='Buses')
    plt.bar(UT+0.2,df6['Trucks, Tempos,MAVs,Tractors - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='yellow',align='center',label='Trucks, Tempos,MAVs,Tractors')
    plt.bar(UT+0.4,df6['Other Motor Vehicles - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='brown',align='center',label='Other Motor Vehicles')
    plt.bar(UT+0.6,df6['Other Vehicles/Objects - Number of Road Accidents - Total - 2014 per 1L people'],width=0.2,color='purple',align='center',label='Other Vehicles/Objects')

    plt.xticks(UT,df6['States/UTs'],rotation='vertical')
    plt.legend(loc="best")
    plt.title("Number of Total Accidents for each vehicle type per 1L people of that state")
    plt.show()

def block6():
    df7 = pd.read_excel('C:/Users/91996/OneDrive/Desktop/Multi-Dimentional-Data-Analytics-of-Road-Accidents-in-India-master/Databases/timeOfOccurence.xls')
    plt.rcParams.update({'font.size'  : 18})
    plt.figure(figsize = (20,10))

    plt.plot(df7['States/Uts'], df7['00-300hrs - Night - 2014'] )
    plt.plot(df7['03-600hrs - Night - 2014'])
    plt.plot(df7['06-900hrs - Day - 2014'])
    plt.plot(df7['09-1200hrs - Day - 2014'])
    plt.plot(df7['12-1500hrs - Day - 2014'])
    plt.plot(df7['15-1800hrs - Day - 2014'])
    plt.plot(df7['18-2100hrs - Night - 2014'])
    plt.plot(df7['21-2400hrs - Night - 2014'])

    plt.title("Line Chart showing accidents occuring as per time of occurence for each state for 2014.")
    plt.xlabel("States/UTs")
    plt.ylabel("Count of Accidents")
    plt.xticks(rotation = 90)
    plt.legend(loc = 'best')
    plt.show()

    dayTime2014 = df7['03-600hrs - Night - 2014']+ df7['06-900hrs - Day - 2014'] + \
                df7['09-1200hrs - Day - 2014']+df7['12-1500hrs - Day - 2014']+df7['15-1800hrs - Day - 2014']
    nightTime2014 = df7['00-300hrs - Night - 2014'] + df7['18-2100hrs - Night - 2014']+df7['21-2400hrs - Night - 2014']
    dayTime2016 = df7['03-600hrs - (Night) - 2016']+ df7['06-900hrs - (Day) - 2016'] + \
                df7['09-1200hrs - (Day) - 2016']+df7['12-1500hrs - (Day) - 2016']+df7['15-1800hrs - (Day) - 2016']
    nightTime2016 = df7['00-300hrs - (Night) - 2016'] + df7['18-2100hrs - (Night) - 2016']+df7['21-2400hrs - (Night) - 2016']
    plt.rcParams.update({'font.size'  : 18})
    plt.figure(figsize = (20,10))
    UT = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])

    plt.bar(UT-0.2, dayTime2014, width = 0.2,label = 'Day Time 2014')
    plt.bar(UT, nightTime2014, width = 0.2, label = 'Night Time 2014')
    plt.bar(UT+0.2, dayTime2016, width = 0.2, label = 'Day Time 2016')
    plt.bar(UT+0.4, nightTime2016, width = 0.2, label = 'Day Time 2016')

    plt.xlabel("States")
    plt.ylabel("Accidents")
    plt.legend(loc = 'best')
    plt.title("Number of Accidents happening in DAY and NIGHT TIME for 2014, 2016.")
    plt.xticks(UT, df7['States/Uts'], rotation=90)
    plt.show()

root = tk.Tk()
root.title("Road Accidents Data Analysis")

window_width = 1000
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Add a background color
root.configure(bg="#f0f0f0")
# Create buttons for each code block

button_width = 40  # Adjust this value as needed

button_padding_x = 3  # Adjust this value for horizontal spacing
button_padding_y = 5  # Adjust this value for vertical spacing



# Create buttons for each code block with the fixed width
button1 = tk.Button(root, text="Analysis of accident per lakh population", command=block1, width=button_width, bg="blue", fg="white",height=button_padding_x)
button2 = tk.Button(root, text="Analysis Rate of accident", command=block2, width=button_width, bg="green", fg="white",height=button_padding_x)
button3 = tk.Button(root, text="Analysis of Accident per Lane", command=block3, width=button_width, bg="red", fg="white",height=button_padding_x)
button4 = tk.Button(root, text="Analysis of Accidents faults/Reasons", command=block4, width=button_width, bg="purple", fg="white",height=button_padding_x)
button5 = tk.Button(root, text="Analysis of Accidents as per vehicle type", command=block5, width=button_width, bg="orange", fg="white",height=button_padding_x)
button6 = tk.Button(root, text="Analysis of number of Accidents as per time", command=block6, width=button_width, bg="gray", fg="white",height=button_padding_x)

button1.pack(pady=10)  
button2.pack(pady=10)  
button3.pack(pady=10)  
button4.pack(pady=10)  
button5.pack(pady=10)  
button6.pack(pady=10)   

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()


root.mainloop()
