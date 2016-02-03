import numpy as np
import datetime
import matplotlib.pyplot as plt
import random

#date1 = datetime.date(1995, 1, 1)
#date2 = datetime.date(2004, 4, 12)
xs = list()
ys = list()

for i in range(0, 1000, 1):
    x = 2*random.random()
    y = 2*random.random()
    if x <= 1:
        if y <= 1:
            continue
        else:
            while y > 1:
                y = 2*random.random()
    else:
        if y >= 1:
            continue
        else:
            while y < 1:
                y = 2*random.random()

    xs.append(x)
    ys.append(y)


x = np.array(xs)
y = np.array(ys)
plt.axis([0, 2, 0, 2])

plt.plot(xs, ys, 'ro')
plt.ylabel('amount of cases passed')
plt.show()