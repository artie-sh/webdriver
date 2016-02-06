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

data = np.random.normal(0.0, 1000.0, 1000)

plt.hist(data, histtype='stepfilled')

fig1 = plt.figure(1)
plt.subplot(221)
#plt.subplot(224)
plt.subplot(222)
#plt.subplot(212)

#plt.axis([0, 2, 0, 2])

plt.title('testing intensity')
plt.xlabel('xlabel here')
plt.ylabel('amount of test cases')



plt.show()