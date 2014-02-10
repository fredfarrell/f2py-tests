import numpy as np

def solve_tridiag_py(a,b,c,v):

    n=len(a)
    
    # Make copies of the b and v variables so that they are unaltered by this function
    bp=np.zeros(n)
    vp=np.zeros(n)
    x=np.zeros(n)

    bp[0]=b[0]
    vp[0]=v[0] 

    for i in range(1,n):
        m = a[i]/bp[i-1]
        bp[i] = b[i] - m*c[i-1]
        vp[i] = v[i] - m*vp[i-1]

    x[n-1]=vp[n-1]/bp[n-1]

    for i in range(n-2,-1,-1):
        x[i] = (vp[i] - c[i]*x[i+1])/bp[i]

    return x

    
