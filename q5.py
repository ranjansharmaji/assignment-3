import numpy as np
def dft(f):
  n=len(f)
  dft=[]
  for q in range(n):
    a=0
    for p in range(n):
      a+=f[p]*np.exp(-2j*np.pi*p*q/n)
    dft.append(a)
  return dft/np.sqrt(n)

question=np.arange(4,100,12)


for i in question:
  arr=np.arange(i)  
  sol2=np.fft.fft(arr)/np.sqrt(i)
  


      