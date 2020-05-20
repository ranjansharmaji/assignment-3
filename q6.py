import numpy as np
import matplotlib.pyplot as plt

n=512
fx=np.ones(n)
dx=1
x=np.arange(n)-(n-1)*dx/2

fk_np=np.fft.fft(fx)/np.sqrt(n)
k=2*np.pi*np.fft.fftfreq(n) 
ft=dx*np.sqrt(n/2/np.pi)*np.exp(-1j*k*x[0])*fk_np

plt.plot(k,np.real(ft))
plt.show() 