import numpy as np
import matplotlib.pyplot as plt

y=[1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]

plt.plot(x,y,linewidth=1.0,c='blue', marker='*')
plt.xlim(0,22)
plt.ylim(1996,2017)
plt.title('Fabiola')
plt.ylabel('anio ')
plt.xlabel('edad ')
plt.savefig('ej1.png')
plt.show() 


