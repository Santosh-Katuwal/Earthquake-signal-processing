import multiprocessing
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pyrotd
pyrotd.processes = 1

cwd=os.getcwd()
acc= pd.read_csv(cwd+'\\test.csv')  #input acceleration must be in terms of [g]
                                    # 1g= 981 gals    --> [gal=cm/s^2]
                                    #if input accln is in cm/s^2: multiply acceleration by (1/981) to convert in terms of g
time_step=0.01
accels=acc.acc_g
osc_damping = 0.05
osc_freqs = np.logspace(-1, 2, 91)
resp_spec = pyrotd.calc_spec_accels(time_step, accels, osc_freqs, osc_damping)

freq=pd.DataFrame(resp_spec.osc_freq)
period=1/freq

period=pd.DataFrame(period)
period.columns=['period']

SA=pd.DataFrame(resp_spec.spec_accel)
SA.columns=['SA']

Data=pd.concat([period,SA],axis=1)
'''
Ref: Smooth Spectra of Horizontal and Vertical Ground Motion(by Praveen K. Malhotra)
DOI:10.1785/0120050062

SD = SA/ω^2 = SV/ω
ω = 2πf= 2π/T
'''

n=len(Data)
SV=[]
SD=[]
for i in range(0,n):
    #Update sv and sd formula when input motion is not in terms of [g]
    sv=981*Data.SA[i]*Data.period[i]/(2*np.pi)      #Note: multiply by 981 only when input acceleration is in terms of g.
                                                    #SV in terms of cm/sec
                                                    #If input motion is in cm/s2: Remove 981 and remaining part will be same
    sd=981*Data.SA[i]*(Data.period[i]/(2*np.pi))**2
    SV.append(sv)
    SD.append(sd)

plt.subplot(3,1,1)
plt.plot(Data.period, Data.SA,label='5% damped spectra',lw=0.8,color='k')
plt.xlabel('Period (Sec)')
plt.ylabel('PSA [g]') #Enter same as input unit
plt.grid(ls='dotted',color='grey')
plt.legend()
plt.xlim(0,4)

plt.subplot(3,1,2)
plt.plot(Data.period, SV,label='5% damped spectra',lw=0.8,color='k')
plt.xlabel('Period (Sec)')
plt.ylabel('PSV [cm/s]') 
plt.grid(ls='dotted',color='grey')
plt.legend()
plt.xlim(0,4)


plt.subplot(3,1,3)
plt.plot(Data.period, SD,label='5% damped spectra',lw=0.8,color='k')
plt.xlabel('Period (Sec)')
plt.ylabel('PSD [cm]') 
plt.grid(ls='dotted',color='grey')
plt.legend()
plt.xlim(0,4)





