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


def UpperEnvelope(nal):
    envelope = zeros(len(nal))
    prevM = 0
    nal[nal<0] = 0
    maxima = argrelmax(nal)[0]

    for x in range(len(maxima)):
        envelope[prevM:maxima[x]] = nal[maxima[x]]
        prevM = maxima[x]
    return abs(envelope)
"""
plt.figure()
plt.plot(signal)
plt.plot(UpperEnvelope(signal))
plt.show()
"""