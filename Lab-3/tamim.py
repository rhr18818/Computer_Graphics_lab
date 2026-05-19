def bresenham(x1, y1, x2, y2):
    x_values = []
    y_values = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x_step = 1 if x2 >= x1 else -1
    y_step = 1 if y2 >= y1 else -1

    m = dy / float(dx) if dx != 0 else None

    # Horizontal line
    if m == 0:
        x, y = x1, y1
        x_values.append(x)
        y_values.append(y)

        for i in range(dx):
            x = x + x_step
            x_values.append(x)
            y_values.append(y)

    # Vertical line
    elif dx == 0:
        x, y = x1, y1
        x_values.append(x)
        y_values.append(y)

        for i in range(dy):
            y = y + y_step
            x_values.append(x)
            y_values.append(y)

    # Slope <= 1
    elif m <= 1:
        dS = 2 * dy
        dT = 2 * (dy - dx)
        d  = 2 * dy - dx

        x, y = x1, y1
        x_values.append(x)
        y_values.append(y)

        while x != x2:
            x = x + x_step

            if d < 0:
                d = d + dS
            else:
                y = y + y_step
                d = d + dT

            x_values.append(x)
            y_values.append(y)

    # Slope > 1
    else:
        dS = 2 * dx
        dT = 2 * (dx - dy)
        d  = 2 * dx - dy

        x, y = x1, y1
        x_values.append(x)
        y_values.append(y)

        while y != y2:
            y = y + y_step

            if d < 0:
                d = d + dS
            else:
                x = x + x_step
                d = d + dT

            x_values.append(x)
            y_values.append(y)

    return x_values, y_values