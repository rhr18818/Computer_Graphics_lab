import matplotlib.pyplot as plt
import numpy as np
import time as t

x_list = []
y_list =[]

for i in range(500):
    x1=np.random.uniform(0,200)
    x2=np.random.uniform(0,200)
    y1=np.random.uniform(0,200)
    y2=np.random.uniform(0,200)
    
    if x1==x2:
        x+=0.0001
    m = (y2-y1)/(x2-x1)
    c = y1 - (m*x1)
    
    X_points = np.linspace(x1,x2,num=100)
    Y_points = m*X_points + c
    x_list.append(X_points)
    y_list.append(Y_points)
    
for i in range(500):
    #plt.scatter(x_list[i],y_list[i])
    plt.plot(x_list[i],y_list[i])


plt.show()