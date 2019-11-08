import given_function

def computations(x0, y0, x, n): #function generate solution for DE using RUnge Kutta method
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    n = int(n)
    h = (x - x0) / n

    for i in range(n - 1):
        x = xs[-1]
        y = ys[-1]

        k1 = h * given_function.function_for_computation(x, y)
        k2 = h * given_function.function_for_computation(x + h/2, y + k1/2)
        k3 = h * given_function.function_for_computation(x + h/2, y + k2/2)
        k4 = h * given_function.function_for_computation(x + h, y + k3)

        x_next = x + h
        y_next = y + k1/6 + k2/3 + k3/3 + k4/6

        xs.append(x_next)
        ys.append(y_next)
    return xs, ys


