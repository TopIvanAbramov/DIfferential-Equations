def computations(x0, y0, x, n): #function generate exact solution for DE
    ys_exact = []
    xs_exact = []

    n = int(n)
    h = (x - x0) / n

    xs_exact.append(x0)
    ys_exact.append(y0)

    c = (y0 + x0) / (x0 * x0)

    for i in range(n - 1):
        x = xs_exact[-1]
        y = c * x * x - x
        x += h
        xs_exact.append(x)
        ys_exact.append(y)

    return xs_exact, ys_exact
