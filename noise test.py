# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:46:24 2017

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

fs = 4000
signal = noise(16000,'brown')
wavwrite("brownNoise.wav",fs,signal)