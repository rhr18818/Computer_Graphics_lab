import matplotlib.pyplot as plt
import numpy as np 
import time as t

def get_dda_points(x1, y1, x2, y2):
    x_pixels = []
    y_pixels = []
    
    dy = y2 - y1
    dx = x2 - x1
    
    if dx == 0 and dy == 0: 
        return [x1], [y1]
        
    if dx == 0:  
        step = 1 if y1 < y2 else -1 
        for y in range(y1, y2 + step, step):
            x_pixels.append(x1)
            y_pixels.append(y)
        return x_pixels, y_pixels

    if dy == 0:  
        step = 1 if x1 < x2 else -1 
        for x in range(x1, x2 + step, step):
            x_pixels.append(x)
            y_pixels.append(y1)
        return x_pixels, y_pixels

    
    m = dy / dx 
    
    if abs(m) <= 1:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        x = x1
        y_f = y1
        
        while x <= x2:
            y = int(np.floor(y_f+0.5))
            x_pixels.append(x)
            y_pixels.append(y)
            
            x += 1
            y_f += m      
            
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        y = y1
        x_f = x1
        m_inv = 1 / m # Same as dx / dy
        
        while y <= y2:
            x = int(np.floor(x_f+0.5))  
            x_pixels.append(x)
            y_pixels.append(y)
            
            y += 1
            x_f += m_inv   
                  
    return x_pixels, y_pixels



start_time = t.time()

x_list = []
y_list = []

total_lines = 500
plt_size = 200

for i in range(total_lines):
    x1=np.random.randint(0,plt_size)
    x2=np.random.randint(0,plt_size)
    y1=np.random.randint(0,plt_size)
    y2=np.random.randint(0,plt_size)
    
    x_point,y_point = get_dda_points(x1,y1,x2,y2)
    
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