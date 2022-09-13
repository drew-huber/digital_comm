import scipy.io
import matplotlib
mat = scipy.io.loadmat('BPAM_MAN_Huber.mat')

import matplotlib.pyplot as plt
plt.plot(mat)
plt.ylabel('some numbers')
plt.show()
