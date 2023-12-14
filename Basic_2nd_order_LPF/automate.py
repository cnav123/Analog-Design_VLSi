# -*- coding: utf-8 -*-
"""
Project: - 2nd Order Low Pass Filter (LPF)
Step:-1 Generate the .txt From .asc files
Created on Thu Dec 14 06:23:59 2023

@author: Admin
"""

#%%
# Step 2: - Automate the process of automaticall varing the log file 
import os
# Step 3: - Run each txt files in Ltspice batch mode using Python scripting
import subprocess

import ltspy3

import matplotlib.pyplot as plt

#Step 2: - Implementation
Txt_original = 'Project_2nd_LPF_TRAN.txt' #
Res1_original = 'Res1=1k'
Cap1_original = 'Cap1=0.1u' # the variable in original file
Res2_original = 'Res2=1k'
Cap2_original = 'Cap2=0.1u'

Res1 = ['Res1=1k', 'Res1=10k']
Res2 = ['Res2=1k', 'Res2=10k']
Cap1 = ['Cap1=0.1u', 'Cap1=1u']
Cap2 = ['Cap2=0.1u', 'Cap2=1u']

# Create a directory to store the files
directory = 'SimFolder'
if not os.path.exists(directory):
    os.makedirs(directory)
    
fig_directory = 'FigFolder'
if not os.path.exists(fig_directory):
    os.makedirs(fig_directory)
    
    
for i in Res1:
    for j in Res2:
        for l in Cap1:
            for m in Cap2:
                with open(Txt_original, 'rb') as file:
                    Data_original = file.read()
                    
                    Data_temp = Data_original.replace(Res1_original.encode('ascii'), i .encode('ascii')).replace(Res2_original.encode('ascii'), j .encode('ascii')).replace(Cap1_original.encode('ascii'), l.encode('ascii')).replace(Cap2_original.encode('ascii'), m .encode('ascii'))
                    # Generate file name based on the combination
                file_name = f'{i}_{j}_{l}_{m}.txt'
                file_name1 = f'{i}_{j}_{l}_{m}'
                
                # Write the modified content to a new file within the directory
                with open(os.path.join(directory, file_name), 'wb') as file:
                    file.write(Data_temp)
                  
                # Change directory to SimFolder before running LTspice
                os.chdir(directory)
                subprocess.call(['c:\Program Files\ADI\LTspice\LTspice.exe', '-b',file_name])
                
                sd = ltspy3.SimData(file_name1 + '.raw') # .raw file in a string
                name = sd.variables # variable names from .raw data
                time_trace = sd.values # time and traces from .raw data
                time = sd.values[0] # The first element is the time as a matrix
                trace = sd.values[1:3] 
                
                plt.figure() # new figure
                plt.plot(time, trace[0], 'ro-')
                plt.plot(time, trace[1], 'b^-')
                plt.xlabel('Time (sec)',fontsize=12, color='black')
                plt.ylabel('Voltage (V)',fontsize=12, color='black')
                plt.title(file_name,fontsize=20)
                plt.legend(['$V_{in}$','$V_{out}$'],fontsize=15)
                plt.grid(True)
                plt.show()
                os.chdir('..') 
                plt.savefig(os.path.join(fig_directory, file_name1 + '.png'), dpi=300) 
                plt.close("all") # close all figures
                


