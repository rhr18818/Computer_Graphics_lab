import matplotlib.pyplot as plt
import numpy as np 

def get_dda_points(x1, y1, x2, y2):
    x_pixels = []
    y_pixels = []
    
    dy = y2 - y1
    dx = x2 - x1
    
    # --- SAFETY CHECKS (Handling Sir's edge cases + backward direction) ---
    
    if dx == 0 and dy == 0:  # Edge case: Start and end are the exact same point
        return [x1], [y1]
        
    if dx == 0:  # Vertical line
        step = 1 if y1 < y2 else -1 # Allow drawing top-down OR bottom-up
        for y in range(y1, y2 + step, step):
            x_pixels.append(x1)
            y_pixels.append(y)
        return x_pixels, y_pixels

    if dy == 0:  # Horizontal line
        step = 1 if x1 < x2 else -1 # Allow drawing right-to-left OR left-to-right
        for x in range(x1, x2 + step, step):
            x_pixels.append(x)
            y_pixels.append(y1)
        return x_pixels, y_pixels

    # --- TEXTBOOK DDA LOGIC ---
    
    m = dy / dx # Safe to calculate slope now
    
    if abs(m) <= 1:
        # Gentle slope: X is the driving axis.
        # FIX: If line is backward (x1 > x2), swap the points so we draw left-to-right
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        x = x1
        y_f = float(y1)
        
        while x <= x2:
            y = round(y_f)
            x_pixels.append(x)
            y_pixels.append(y)
            
            x += 1
            y_f += m      
            
    else:
        # Steep slope: Y is the driving axis.
        # FIX: If line is backward (y1 > y2), swap the points so we draw bottom-to-top
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            
        y = y1
        x_f = float(x1)
        m_inv = 1 / m # Same as dx / dy
        
        while y <= y2:
            x = round(x_f)  
            x_pixels.append(x)
            y_pixels.append(y)
            
            y += 1
            x_f += m_inv   
                  
    return x_pixels, y_pixels

# ==========================================
# MAIN EXECUTION
# ==========================================

plt_size = 100

# Use randint() instead of uniform() to ensure we start on exact whole pixels
x1 = np.random.randint(0, plt_size)
x2 = np.random.randint(0, plt_size)
y1 = np.random.randint(0, plt_size)
y2 = np.random.randint(0, plt_size)

print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2})")

# Get the calculated pixels
X, Y = get_dda_points(x1, y1, x2, y2)

# Plot the pixels
# Note: Because the grid is 100x100, markersize=10 is too big. 
# Reduced markersize so they look like tiny pixels on a large grid.
plt.plot(X, Y, marker='s', color='black', markersize=3, linestyle='')

# Draw the grid
plt.grid(True, which='both', color='lightgray', linestyle='-', alpha=0.5)

# # Force the canvas to stay a consistent size
# plt.xlim(0, plt_size)
# plt.ylim(0, plt_size)

plt.title("DDA Rasterization (Random Line)")
plt.xlabel("X Pixels")
plt.ylabel("Y Pixels")

plt.show()