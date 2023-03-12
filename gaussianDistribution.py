import numpy as np
import matplotlib.pyplot as plt

#Sample 100 points from
#Gaussian dist. with mean 5 and  variance 1
s = np.random.normal(5, 1, 100)

#Visualise
plt.plot(s,np.zeros(len(s)),'ro')
plt.axis([0,10,-0.01, 1])
plt.show()
