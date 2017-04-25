# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:45:34 2017

@author: Mauritszzzz
"""
import random
from math import *
from scipy import *
from scipy.io import wavfile
from scipy.signal import *
import matplotlib
#matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
from scipy.fftpack import *
from functies import *


[fs, signal] = wavfile.read("riet.wav")

mono_signal = signal.sum(axis=1)/2
signal2 = mono_signal


new = mono_signal
new[new<500] = 0
maxim =  argrelmax(new)
maxima = maxim[0]
envelope = zeros(len(maxima))
envelope2 = abs(hilbert(signal2))

for x in range(0,len(maxima)):
    factor = int(len(envelope)/len(maxima))
    envelope[x*factor : (x*factor) +factor] = ones(factor)*mono_signal[maxima[x]]
  
    
plt.figure()
plt.plot(signal2)
plt.show()

plt.figure()
plt.plot(signal2[0:500],color='g')
plt.plot(abs(envelope[0:500]), color='r')
#plt.plot(abs(envelope2[0:500]))
plt.show()



signaal_f = abs(fft(mono_signal[0:1000]))


noise = noiseGen(len(mono_signal),1)

"""
#spectrogram(noise,44100)
fs = 4000;
b,a = iirfilter(5,0.4,btype="lowpass",ftype="butter")
result = lfilter(b,a,noise) * 0.000004
"""
result = noise*envelope2
plt.figure()
#plt.yscale('log')
plt.plot(result, color='r')
plt.plot(signal2)
plt.show()
wavwrite("noise.wav",fs,result)

"""

# recreate omhullende
e = 0.55
b = 7
n= 40
meixner_1 = meixner(e,b,n)
meixner_ = zeros(len(meixner_1)*5000)
for i in range(len(meixner_1)-1):
    if meixner_1[i] != 0 and meixner_1[1+1] != 0:
     print("i = ", meixner_1[i])
     print("\n i+1 = ", meixner_1[i+1])
     row =  arange(meixner_1[i],meixner_1[i+1],(meixner_1[i+1]-meixner_1[i])/5000)
     meixner_[i*5000 : (i+1)*5000] = row
    else:
     meixner_[i*5000 : (i+1)*5000] = zeros(5000)
    
#plt.figure()
plt.plot(meixner_)
plt.show()
"""