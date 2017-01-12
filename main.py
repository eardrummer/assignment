import sys
sys.path.append('../../software/models/')
import utilFunctions as UF
import numpy as np
from sineModel import sineModelMultiRes
from scipy.signal import get_window

fs, x = UF.wavread('Synth2.wav')

N1 = 2048
N2 = 1024
N3 = 512

B1 = np.array([0,500])
B2 = np.array([500,2000])
B3 = np.array([2000,22050])

w1 = get_window('blackman', N1 - 1)
w2 = get_window('blackman', N2 - 1)
w3 = get_window('blackman', N3 - 1)

w_k = np.array([w1,w2,w3])
N_k = np.array([N1,N2,N3])
B_k = np.array([B1,B2,B3])

t = -100

y = sineModelMultiRes(x,fs,w_k,N_k,t,B_k)

UF.wavwrite(y,fs,'output.wav')
