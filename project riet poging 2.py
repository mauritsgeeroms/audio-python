# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:53:17 2017

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
from noisegenerator import noise
from envelope import *

[fs, sal] = wavfile.read("riet.wav")


#venster 1: golf van geluid
n= 155000
#Bnoise = noise(len(signal),'brown')
pinkNoise = noise(n,'pink')*8000


envelope = gaussian(n,40600)*4000


#result = Bnoise*60000000
venster1 = envelope*pinkNoise

#venster2: lage amplitude ruis
signal = sal[0:155000]
pinkNoise = noise(len(signal),'pink')*6000*1500
venster2 = pinkNoise


totaal = zeros(len(venster1)*2)
totaal[0:155000] = venster2
totaal[145000:300000]= venster1

plt.figure()
plt.plot(sal[0:300000])
#plt.plot(envelope, color='r')
plt.plot(totaal)
plt.show()

wavwrite("rietNoise.wav",fs,result)
