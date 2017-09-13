import numpy as np
import matplotlib.pyplot as plt

#magnitud=3,constante=2014
def f(t):
    return 3.0*np.cos(2*np.pi*t)+2014
t=np.arange(0.0,1.0,0.03)

plt.plot(t,f(t),'b--')
plt.title('grafica 2')
plt.savefig('ej2.png')
plt.show() 


