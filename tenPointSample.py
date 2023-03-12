import numpy as np
import matplotlib.pyplot as plt

# Sample 3 points from
# uniform dist. between 0 and 10
s = np.random.uniform(0, 10, 10)

# Visualise
plt.plot(s,np.zeros(len(s)),'ro')
plt.axis([0,10,-0.01, 1])
plt.show()
