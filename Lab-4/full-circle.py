#full circle drawing with bresenham

import matplotlib.pyplot as plt

def get_bresenham_circle_points(h, k, r):
    x_pixels = []
    y_pixels = []
    
    x = 0
    y = r
    d = 3 - 2 * r
    
    
    def plot_8_octants(x_val, y_val):
        #(xc, yc) to shift the circle to wherever we want it
        points = [
            (h + x_val, k + y_val), 
            (h - x_val, k + y_val), 
            (h + x_val, k - y_val), 
            (h - x_val, k - y_val), 
            (h + y_val, k + x_val), 
            (h - y_val, k + x_val), 
            (h + y_val, k - x_val), 
            (h - y_val, k - x_val)  
        ]
        for px, py in points:
            x_pixels.append(px)
            y_pixels.append(py)

    while x <= y:
        
        plot_8_octants(x, y)
        
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1    
            
        x += 1        
        
    return x_pixels, y_pixels

#Plotting the Circle

center_x = 0
center_y = 0
radius = 50

x_list, y_list = get_bresenham_circle_points(center_x, center_y, radius)


# plt.figure(figsize=(6, 6)) 

plt.scatter(x_list, y_list, color='blue', s=15, marker='s') 

plt.title(f"Bresenham's Circle Algorithm\nCenter: ({center_x}, {center_y}) | Radius: {radius}")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# makes the X and Y axes have the exact same scale or give figsize square Matplotlib stretches the circle into an oval/ellipse!
plt.axis('equal') 

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()