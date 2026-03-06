# Draw 500 straight lines with random starting and ending points within a single plot and calculate the time needed to find the points for them.

import matplotlib.pyplot as plt
import numpy as np 
import time as t

start_time = t.time()

all_x_arrays = []
all_y_arrays = []

lines_num = 500
plot_size = 200

points_per_line = 100

for _ in range(lines_num):
    x1 = np.random.uniform(0,plot_size)
    y1 = np.random.uniform(0,plot_size)
    x2 = np.random.uniform(0,plot_size)
    y2 = np.random.uniform(0,plot_size)
    
    #prevent division by 0
    if x1==x2:
        x2 += 0.0001
    
    m = (y2-y1)/(x2-x1)
    c = y1 - (m*x1)
    
    X_points = np.linspace(x1,x2,points_per_line) # give 100 values for x
    
    Y_points = m*X_points + c
    
    #append a sinlge line coordinate
    all_x_arrays.append(X_points) 
    all_y_arrays.append(Y_points)
    
# print(all_x_arrays[0])
end_time = t.time()
time_taken = end_time-start_time

print(f"Time taken to calculated point {lines_num} lines: {time_taken:.5f} seconds")


# Plotting the Results

print("Drawing the lines...")
# plt.figure(figsize=(6, 6))
# plt.plot(all_x_arrays,all_y_arrays)
for i in range(lines_num):
    plt.plot(all_x_arrays[i],all_y_arrays[i],linewidth=0.9)


plt.title(f"{lines_num} Lines generated, Time Taken:{time_taken:.5f}s")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# plt.grid(True)
# plt.xlim(0, 100)
# plt.ylim(0, 100)
plt.show()
