import matplotlib.pyplot as plt
import numpy as np 
import time as t


def get_dda_points(x1, y1, x2, y2):
    x_pixels, y_pixels = [], []
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
        x, y_f = x1, y1
        while x <= x2:
            y = int(np.floor(y_f + 0.5))
            x_pixels.append(x)
            y_pixels.append(y)
            x += 1
            y_f += m      
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y, x_f = y1, x1
        m_inv = 1 / m 
        while y <= y2:
            x = int(np.floor(x_f + 0.5))  
            x_pixels.append(x)
            y_pixels.append(y)
            y += 1
            x_f += m_inv   
                  
    return x_pixels, y_pixels


def get_bresenham_points(x1, y1, x2, y2):
    x_pixels, y_pixels = [], []
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1
    
    x, y = x1, y1
    
    if dx > dy:
        dS = 2 * dy
        dT = 2 * (dy - dx)
        d = 2 * dy - dx
        for _ in range(dx + 1): 
            x_pixels.append(x)
            y_pixels.append(y)
            if d < 0:
                d += dS
            else:
                d += dT
                y += step_y 
            x += step_x     
    else:
        dS = 2 * dx
        dT = 2 * (dx - dy)
        d = 2 * dx - dy
        for _ in range(dy + 1): 
            x_pixels.append(x)
            y_pixels.append(y)
            if d < 0:
                d += dS
            else:
                d += dT
                x += step_x 
            y += step_y     
                          
    return x_pixels, y_pixels

total_lines = 500
plt_size = 200


lines_data = []
for i in range(total_lines):
    x1 = np.random.randint(0, plt_size)
    x2 = np.random.randint(0, plt_size)
    y1 = np.random.randint(0, plt_size)
    y2 = np.random.randint(0, plt_size)
    lines_data.append((x1, y1, x2, y2))


start_time = t.time()
dda_x_list =[]
dda_y_list = []
for x1, y1, x2, y2 in lines_data:
    x_pt,y_pt= get_dda_points(x1, y1, x2, y2) 
    dda_x_list.append(x_pt)
    dda_y_list.append(y_pt)
end_time = t.time()
dda_time_taken = end_time - start_time



start_time = t.time()
bres_x_list = []
bres_y_list = []
for x1, y1, x2, y2 in lines_data:
    x_pt, y_pt = get_bresenham_points(x1, y1, x2, y2)
    bres_x_list.append(x_pt)
    bres_y_list.append(y_pt)
end_time = t.time()
bres_time_taken = end_time - start_time

# --- Console Report ---
if bres_time_taken < dda_time_taken:
    conclusion = "Bresenham is FASTER"
else:
    conclusion = "Times are similar, but Theoritically Bresenham Faster"

print("-" * 40)
print(f"PERFORMANCE REPORT ({total_lines} lines):")
print("-" * 40)
print(f"DDA Time       : {dda_time_taken:.6f} seconds")
print(f"Bresenham Time : {bres_time_taken:.6f} seconds")
print("-" * 40)
print(f"Conclusion: {conclusion}")
print("-" * 40)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Plot all DDA lines on the first subplot (ax1)
for i in range(total_lines):
    ax1.plot(dda_x_list[i], dda_y_list[i])

ax1.set_title(f"DDA Algorithm\nTime: {dda_time_taken:.5f}s", fontweight='bold')
ax1.set_xlabel("X Axis")
ax1.set_ylabel("Y Axis")
ax1.grid(True, linestyle='--', alpha=0.5) # Adding a light grid looks professional

# Plot all Bresenham lines on the second subplot (ax2)
for i in range(total_lines):
    ax2.plot(bres_x_list[i], bres_y_list[i])

ax2.set_title(f"Bresenham Algorithm\nTime: {bres_time_taken:.5f}s", fontweight='bold')
ax2.set_xlabel("X Axis")
ax2.set_ylabel("Y Axis")
ax2.grid(True, linestyle='--', alpha=0.5)

# Set a massive master title over the whole window
fig.suptitle(f"Algorithm Comparison: {total_lines} Identical Lines\nConclusion: {conclusion}", 
             fontsize=14, fontweight='bold', color='darkblue')

# Adjust layout so titles don't overlap
plt.tight_layout()

plt.show()