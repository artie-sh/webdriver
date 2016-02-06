import numpy as np
import datetime
import matplotlib.pyplot as plt
import random
#import pylab as pl
import math


xs1 = list()
ys1 = list()
xs2 = list()
ys2 = list()


for x in range(-500, 500, 1):
    y = math.sin(x)

    xs1.append(x)
#    xs2.append(x)
    ys1.append(y)
#    y = 0.32*x + 0.2
 #   ys2.append(y)

'''    if x <= 1:
        if y <= 1:
            continue
        else:
            while y > 1:
                y = 2*np.random.normal()
    else:
        if y >= 1:
            continue
        else:
            while y < 1:
                y = 2*np.random.normal()
'''


plt.xlim(-1000, 1000)
plt.ylim(-1000, 1000)

#plt.axis([0, 2, 0, 2])

plt.title('testing intensity')
plt.xlabel('xlabel here')
plt.ylabel('amount of test cases')

plot1 = tuple(plt.plot(xs1, ys1, 'r'))
plot2, = plt.plot(xs2, ys2, 'go')
plt.legend((plot1, plot2), ('ys1', 'ys2'))

plt.show()