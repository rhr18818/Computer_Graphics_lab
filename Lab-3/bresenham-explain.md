**Bresenham’s Line Algorithm**. 

**Bresenham's algorithm was invented specifically to avoid calculating the slope $m$**. 
In the DDA algorithm you showed previously, calculating $m = dy/dx$ creates a floating-point number (a decimal). Computers process integer math (whole numbers) much faster than floating-point math. Bresenham's brilliant realization was that we can draw a perfect line using **only integer addition and subtraction**.

Here is how the theory you learned connects to this code, followed by a step-by-step breakdown.

---

### The Big Connection: Slope ($m$) vs. Deltas ($dx, dy$)
In theory, you learned:
*   **Case 1 (Shallow Line):** $|m| \le 1$. The line is more horizontal. We step $X$ by 1, and decide whether to increment $Y$.
*   **Case 2 (Steep Line):** $|m| > 1$. The line is more vertical. We step $Y$ by 1, and decide whether to increment $X$.

**How the code translates this without calculating $m$:**
We know that $m = \frac{dy}{dx}$.
*   If $m < 1$, that mathematically means $\frac{dy}{dx} < 1$, which means **$dx > dy$**.
*   If $m > 1$, that mathematically means $\frac{dy}{dx} > 1$, which means **$dy > dx$**.

So, when the code says `if dx > dy:`, it is exactly the same as saying `if abs(m) < 1:`. It just avoids the slow division operation!

---

### 1. Setup and Direction (Octant Logic)
```python
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)
    
    x = x1
    y = y1
    
    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1
```
*   **Theory:** In DDA, we had to swap points to make sure we always drew from left-to-right or bottom-to-top. Bresenham handles all directions (all 8 octants of a graph) gracefully. We use absolute values for $dx$ and $dy$ so our math always works with positive distances.
*   We use `step_x` and `step_y` to remember which direction we are walking. 
*   **Example:** If we draw from `(5, 5)` to `(2, 8)`. 
    *   $dx = |2 - 5| = 3$. $dy = |8 - 5| = 3$.
    *   `step_x = -1` (since $5 > 2$, X needs to go backward).
    *   `step_y = 1` (since $5 < 8$, Y goes forward).

---

### 2. Condition 1: Shallow Slope (`dx > dy` / $|m| < 1$)
```python
    if dx > dy:
        dS = 2*dy
        dT = 2*(dy-dx)
        d = 2*dy - dx
        
        for i in range(dx+1): 
            x_pixels.append(x)
            y_pixels.append(y)
            if(d < 0):
                d += dS
            else:
                d += dT
                y += step_y
            x += step_x
```
*   **Theory:** Because $dx > dy$, X is our primary driving axis. We will confidently step X exactly once every loop (`x += step_x`). The only question is: **Do we also step Y, or keep Y the same?**
*   **The Decision Parameter (`d`):** Instead of keeping track of decimals (like `y_f += m` in DDA), we use `d`. 
    *   If `d < 0`: The true mathematical line is closer to our current Y. Keep Y the same. Update `d` by adding `dS`.
    *   If `d >= 0`: The true mathematical line has crossed the halfway point to the next pixel. Step Y up/down (`y += step_y`). Update `d` by adding `dT`.
*   **Example:** Draw from `(1, 1)` to `(4, 2)`.
    *   $dx = 3$, $dy = 1$. (Shallow, so we enter this block). `step_x = 1`, `step_y = 1`.
    *   `dS = 2*1 = 2`.
    *   `dT = 2*(1-3) = -4`.
    *   Initial `d = 2(1) - 3 = -1`.
    *   **Loop 1 (i=0):** Plot `(1, 1)`. `d` is `-1` (Negative). Keep Y same. New `d = -1 + 2 = 1`. Step X to `2`.
    *   **Loop 2 (i=1):** Plot `(2, 1)`. `d` is `1` (Positive!). Step Y to `2`. New `d = 1 + (-4) = -3`. Step X to `3`.
    *   **Loop 3 (i=2):** Plot `(3, 2)`. `d` is `-3` (Negative). Keep Y same. New `d = -3 + 2 = -1`. Step X to `4`.
    *   **Loop 4 (i=3):** Plot `(4, 2)`. (Loop finishes).

---

### 3. Condition 2: Steep Slope (`else` / `dy >= dx` / $|m| \ge 1$)
```python
    else:
        dS = 2*dx
        dT = 2*(dx-dy)
        d = 2*dx - dy
        for i in range(dy+1): 
            x_pixels.append(x)
            y_pixels.append(y)
            if(d < 0):
                d += dS
            else:
                d += dT
                x += step_x   
            y += step_y
```
*   **Theory:** Because $dy \ge dx$, Y is our primary driving axis (the line is steep). We confidently step Y every loop (`y += step_y`). The question is: **Do we step X?**
*   Notice how **all the variables are perfectly swapped** compared to the first condition. `dS`, `dT`, and `d` are calculated with $dx$ and $dy$ flipped. Inside the loop, `d < 0` means we keep X the same, and `d >= 0` means we step X.
*   **Example:** Draw from `(0, 0)` to `(1, 3)`.
    *   $dx = 1$, $dy = 3$. (Steep, so we enter the `else` block). `step_x = 1`, `step_y = 1`.
    *   `dS = 2*1 = 2`.
    *   `dT = 2*(1-3) = -4`.
    *   Initial `d = 2(1) - 3 = -1`.
    *   **Loop 1:** Plot `(0, 0)`. `d < 0`. Keep X. `d = -1 + 2 = 1`. Step Y to `1`.
    *   **Loop 2:** Plot `(0, 1)`. `d > 0`. Step X to `1`. `d = 1 + (-4) = -3`. Step Y to `2`.
    *   **Loop 3:** Plot `(1, 2)`. `d < 0`. Keep X. `d = -3 + 2 = -1`. Step Y to `3`.
    *   **Loop 4:** Plot `(1, 3)`. (Loop ends).

---

### 4. The Testing Code
The entire second half of the script:
```python
start_time = t.time()
# ... random number generation ...
# ... plotting ...
plt.title(f"{total_lines} Lines generated by Bresenham, Time taken:{time_taken:.5f}s")
```
This is functionally **identical** to your DDA code. The purpose of this is performance testing.

Because Bresenham's algorithm does not use division (`/`), does not use floating point numbers (decimals), and does not use rounding (`np.floor`), it is computationally "cheaper". Historically (and often still today on basic hardware), if you compare the `time_taken` output of the DDA script and this Bresenham script, **Bresenham will run faster**, while drawing exactly the same high-quality lines!