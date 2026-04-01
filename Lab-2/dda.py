import matplotlib.pyplot as plt
import numpy as np 
import time as t

# ### m=0 ,m=inf hoile ki korte hobe?
# x_values = []
# y_values = []
# if m ==0:
#     while(x<=x2):
#         x_values.append(x)
#         x++
#         y_values.append(y)
# eles if(x2-x1)==0:
#     while(y<=y2):
#         x_values.append(x)
#         y_values.append(y)
#         y++
        

def get_dda_points(x1, y1, x2, y2):
    x_pixels =[]
    y_pixels = []
    
    dy = y2 - y1
    dx = x2 - x1
    
    # --- SAFETY CHECKS (From your Sir) ---
    if dx == 0:  # Vertical line
        while y1 <= y2:
            x_pixels.append(x1)
            y_pixels.append(y1)
            y1 += 1
        return x_pixels, y_pixels

    if dy == 0:  # Horizontal line
        while x1 <= x2:
            x_pixels.append(x1)
            y_pixels.append(y1)
            x1 += 1
        return x_pixels, y_pixels

    # Calculate Slope
    m = dy / dx
    
    if abs(m)<=1:
        x=x1
        y_f = y1
        while x <= x2:
            y=round(y_f)
            x_pixels.append(x)
            y_pixels.append(y)
            
            x += 1
            y_f += m      
    else:
      y=y1
      x_f = x1
      m_inv = 1/m
      while y <= y2:
          x = round(x_f)  
          x_pixels.append(x)
          y_pixels.append(y)
          
          y+=1
          x_f+=m_inv   
                  
    return x_pixels, y_pixels



x1,x2=2,10
y1,y2=2,6

X,Y = get_dda_points(x1,y1,x2,y2)
print(X)
# plt.scatter(X,Y)
# plt.plot(X,Y)

plt.plot(X, Y, marker='s', color='black', markersize=10, linestyle='')

# Draw a grid so it looks like a computer screen
plt.grid(True, which='both', color='lightgray')
plt.xticks(range(0, 12))
plt.yticks(range(0, 8))

plt.title("DDA Rasterization (Pixels on a Screen)")

plt.show()

