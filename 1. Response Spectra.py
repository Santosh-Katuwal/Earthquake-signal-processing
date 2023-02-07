import multiprocessing
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pyrotd
pyrotd.processes = 1

cwd=os.getcwd()
acc= pd.read_csv(cwd+'\\test.csv')
time_step=0.01
accels=acc.acc_g
osc_damping = 0.05
osc_freqs = np.logspace(-1, 2, 91)
resp_spec = pyrotd.calc_spec_accels(time_step, accels, osc_freqs, osc_damping)

freq=pd.DataFrame(resp_spec.osc_freq)
period=1/freq

plt.figure(1)
plt.plot(period, resp_spec.spec_accel,label='5% damped spectra',lw=0.8,color='k')
plt.xlabel('Period (Sec)')
plt.ylabel('Spectral Acceleration [g]') #Enter same as input unit
plt.grid(ls='dotted',color='grey')
plt.legend()
plt.xlim(0,4)



