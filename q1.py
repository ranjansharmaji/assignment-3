import numpy as np
import matplotlib.pyplot as plt 

n=512  
dx=1
xmin=-(n-1)*dx/2 

x=np.zeros(n)
k=np.zeros(n) 
fx=np.zeros(n)
fk=np.zeros(n)
i=0
while i in range(n):
  x[i]=xmin+i*dx 
  if x[i]==0:
    fx[i]=1
  else:
    fx[i]=np.sin(x[i])/x[i] 
  i=i+1
dft=np.fft.fft(fx)/np.sqrt(n) 
k=2*np.pi*np.fft.fftfreq(n,dx)

l=np.argsort(k)
k=k[l]
dft=dft[l]

fk=dx*np.sqrt(n/(2.0*np.pi))*np.exp(-1j*k*xmin)*dft    

def box(k):
  box=np.zeros(len(k)) 
  for i in range(len(k)):
    if abs(k[i])<1:
      box[i]=np.sqrt(np.pi/2)
  return box

plt.plot(k,box(k),'*',label='analytic') 
plt.plot(k,np.real(fk),label='numerical')

plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()
plt.show()   