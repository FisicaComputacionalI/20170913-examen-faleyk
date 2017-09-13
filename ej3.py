import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return 3.0*np.cos(2*np.pi*t)+2014
t=np.arange(0.0,1.0,0.03)

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
y=[1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

plt.figure(1)
plt.subplot(211)
plt.plot(t,f(t),'b--',x,y,'r--')
plt.xlim(0,5)
plt.title('encimadas')
plt.subplot(212)
plt.plot(t,f(t),'b--')
plt.title('trigonometrica')
plt.savefig('ej3.png')
plt.show() 


