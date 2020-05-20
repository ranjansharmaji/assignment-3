import numpy as np
import matplotlib.pyplot as plt

f1='C:/Users/ranja/Desktop/A3/noise.txt'
data=np.loadtxt(f1,usecols=0)

n=len(data)
x=np.arange(n)

dft=np.fft.fft(data)
k=2*np.pi/n*(np.arange(n)-n/2) 
l=np.argsort(k)
dft=dft[l]

periodogram=abs(dft)*abs(dft)/n


plt.plot(x,data,label='data')
plt.xlabel('x')


plt.plot(k,np.real(dft),label='dft')
plt.xlabel('k')




plt.show()


