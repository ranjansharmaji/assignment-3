import numpy as np
import matplotlib.pyplot as plt

def box(r):
  box=np.zeros(len(r))
  for i in range(len(r)):
    if abs(r[i])<1:
      box[i]=1
  return box 

n=512
xmin=-4
xmax=4
dx=(xmax-xmin)/(n-1) 

i=0
x=np.zeros(n) 
fx=np.zeros(2*n)
while i in range(n):
  x[i]=xmin+i*dx
  if abs(x[i])<1:
    fx[i]=1
  i=i+1 
dft=np.fft.fft(fx)/np.sqrt(n)
mult=dft*dft
IT=np.fft.ifft(mult)*np.sqrt(n)
IT=dx*np.sqrt(n)*IT 

x_new=np.linspace(-(n-1)*dx/2,(n-1)*dx/2,2*n) 
plt.plot(x_new,np.real(IT))
plt.plot(x,box(x))
plt.xlabel('x')
plt.ylabel('f')
plt.show() 