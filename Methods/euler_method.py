import given_function

def computations(x0, y0, x, n): #function generate solution for DE using Euler method
    xs = []
    ys = []

    xs.append(x0)
    ys.append(y0)

    n = int(n)
    h = (x - x0) / n

    for i in range(n - 1):
        x = xs[-1]
        y = ys[-1]

        x_next = x + h
        f = given_function.function_for_computation(x, y)
        y_next = y + h * f

        xs.append(x_next)
        ys.append(y_next)
    return xs, ys


