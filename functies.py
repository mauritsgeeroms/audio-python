import random
from math import *
from scipy import *
from scipy.io import wavfile
from scipy.signal import *
import matplotlib
#matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
from scipy.fftpack import *
from numpy import pi, polymul
from scipy.signal import bilinear, lfilter

def getParameters(x):
    x_f = abs(fft(x))
    mean = mean(x_f)
    std = std(x_f)
    freq = zeros(len(x))
    for i in range(len(x)):
        if x_f[i] > (mean-2*std):
            freq[i] = x_f[i]
    return freq

def A_weighting(fs):
    """Design of an A-weighting filter.
    b, a = A_weighting(fs) designs a digital A-weighting filter for
    sampling frequency `fs`. Usage: y = scipy.signal.lfilter(b, a, x).
    Warning: `fs` should normally be higher than 20 kHz. For example,
    fs = 48000 yields a class 1-compliant filter.
    References:
       [1] IEC/CD 1672: Electroacoustics-Sound Level Meters, Nov. 1996.
    """
    # Definition of analog A-weighting filter according to IEC/CD 1672.
    f1 = 20.598997
    f2 = 107.65265
    f3 = 737.86223
    f4 = 12194.217
    A1000 = 1.9997

    NUMs = [(2*pi * f4)**2 * (10**(A1000/20)), 0, 0, 0, 0]
    DENs = polymul([1, 4*pi * f4, (2*pi * f4)**2],
                   [1, 4*pi * f1, (2*pi * f1)**2])
    DENs = polymul(polymul(DENs, [1, 2*pi * f3]),
                                 [1, 2*pi * f2])

    # Use the bilinear transformation to get the digital filter.
    # (Octave, MATLAB, and PyLab disagree about Fs vs 1/Fs)
    return bilinear(NUMs, DENs, fs)


def coswav(f,fs,duur):
	lengte=fs*duur
	stap=2*pi*f/fs
	return cos(arange(0,lengte*stap,stap))
	
def wavwrite(filename,fs,signaal):
	normalized=int16(signaal/max(fabs(signaal))*32767)
	wavfile.write(filename,fs,normalized)
	
def spectrogram(signaal,fs):
	plt.figure()
	plt.specgram(signaal,NFFT=1024,Fs=fs,noverlap=512)
	plt.show()
    
def ph(getal,n):
    return (factorial(getal+n-1)/factorial(n-1))

def meixner(e,b,n):
    meixners = zeros(n)
    for i in range(1,n):
        meixners[i] = pow((1-(e*e)),b/2) * sqrt(ph(b,i)/factorial(i)) * pow(e,i) 
    return meixners
def noiseGen(length,maxi):
    return (random.rand(length)*maxi*2 - maxi)

