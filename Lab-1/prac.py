import matplotlib.pyplot as plt
import numpy as np 
import time as t

start_time = t.time()

x_list = []
y_list = []

total_lines = 500
plt_size = 200

total_point_in_one_line = 100

for i in range(total_lines):
    x1=np.random.uniform(0,plt_size)
    x2=np.random.uniform(0,plt_size)
    y1=np.random.uniform(0,plt_size)
    y2=np.random.uniform(0,plt_size)
    
    # if x1==x2:
    #     x2+=0.0001
    # m = (y2-y1)/(x2-x1)
    # c = y1 - (m*x1)
    
    # x_point = np.linspace(x1,x2,total_point_in_one_line)
    # y_point = m*x_point + c
    
    x_point = [x1,x2]
    y_point = [y1,y2]
    
    x_list.append(x_point)
    y_list.append(y_point)

ent_time = t.time()
time_taken = ent_time- start_time

for i in range(total_lines):
    plt.plot(x_list[i],y_list[i])

plt.title(f"{total_lines} Lines generated, Time taken:{time_taken:.5f}s")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()