import numpy as np

n=512
dx=0.5
xmin=-(n-1)*dx/2
xmax=xmin+(n-1)*dx 

x=np.linspace(xmin,xmax,n)
y=x
[X,Y]=np.meshgrid(x,y)

F=np.exp(-X**2-Y**2) 

kx=2*np.pi/(n*dx)*(np.arange(n)-n/2)
ky=kx
[KX,KY]=np.meshgrid(kx,ky)

dft=np.fft.fft2(F)/n 

k=np.fft.fftfreq(n,dx)
l=np.argsort(k)
for i in range(n):
  dft[i]=dft[i][l]
for i in range(n):
  dft[:,i]=dft[:,i][l]
  
dft=(dx*np.sqrt(n/(2*np.pi)))**2*np.exp(-1j*(KX+KY)*xmin)*dft 

#analytic 
F_a=np.exp(-(KX**2+KY**2)/4)/2



















 

 