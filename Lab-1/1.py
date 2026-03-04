import matplotlib.pyplot as plt
import numpy as np 

m,c = 2,3


# Y = np.array([])
X = np.linspace(1,10,num=100)

# for x in X:
#     y = m*x +c
#     Y = np.append(Y,y)
Y = m*X + c

# print(X)
print(Y)

plt.plot(X,Y)
plt.show()

