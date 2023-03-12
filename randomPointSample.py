import numpy as np
import matplotlib.pyplot as plt

# Sample 3 points from
# uniform dist. between 0 and x
s = np.random.uniform(0, 10, 50)

# Visualise
plt.plot(s,np.zeros(len(s)),'ro')
plt.axis([0,10,-0.01, 1])
plt.show()
