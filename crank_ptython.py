import numpy as np
from matplotlib import pyplot as plt
import tridiag

#define parameters
N=10000

dx=0.4
dt=0.1

Diff=100.0

tfinal=50

R=Diff*dt/(dx*dx)

#initialize arrays
c_new = np.zeros(N)
c_old = np.zeros(N)
a = np.zeros(N)
b = np.zeros(N)
c = np.zeros(N)
d = np.zeros(N)

#initial condition for concentration c
for i in range(N):
    c_new[i] = np.exp(-(i-N/2)*(i-N/2)/10000.0)

f = open('init.dat','w')

#write initial condition to a file
for x in c_new:
    f.write('{0}\n'.format(x))


for i in range(tfinal):
    
    c_old[:]=c_new
    
    #fill a,b,c,d arrays

    a[:]=-R
    b[:]=1+2*R
    c[:]=-R

    for i in range(1,N-1):
        d[i] = R*c_old[i-1]+(1-2*R)*c_old[i]+R*c_old[i+1]
    
    #boundary conditions
    a[0]=0
    b[0]=1
    c[0]=-1
    d[0]=0

    a[N-1]=-1
    b[N-1]=1
    c[N-1]=0
    d[N-1]=0

    c_new = tridiag.solve_tridiag(a,b,c,d)


g = open('final_python.dat','w')

#write initial condition to a file
for x in c_new:
    g.write('{0}\n'.format(x))

ax = plt.axes(xlim=(0,N),ylim=(0,1))
xaxis = np.arange(N)
ax.plot(xaxis,c_new,'b-',lw=2)
plt.xlabel("x")
plt.show()


