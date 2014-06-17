import scipy as sp
from scipy import linalg,sparse
import scipy.sparse.linalg
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import tridiag

#define parameters
N=10000

dx=0.4
dt=0.2

Diff=100.0

tfinal=100

R=Diff*dt/(dx*dx)

#initialize arrays
c_new = sp.zeros(N)
c_old = sp.zeros(N)
c_init = sp.zeros(N)
a = sp.zeros(N)
b = sp.zeros(N)
c = sp.zeros(N)
d = sp.zeros(N)

#initial condition for concentration c
for i in range(N):
    c_init[i] = sp.exp(-(i-N/2)*(i-N/2)/10000.0)
    c_new[i] = c_init[i]


#loop through time
for i in range(tfinal):   

    c_old=c_new
    
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

    #invert the sparse matrix using scipy bicg routine
    A = sp.sparse.spdiags([a,b,c],[-1,0,1],N,N)
    c_new = sp.sparse.linalg.bicg(A,d)[0]

plt.plot(c_init)
plt.plot(c_new)
plt.show()

