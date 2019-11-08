from Methods import euler_method, improved_euler_method, runge_kutta_method, exact_solution
from matplotlib import pyplot as plt
import os


def analysis(x0, y0, x, n): #function analyze errors graphs of global errors for DE

    max_error_euler = []
    max_error_improved_euler = []
    max_error_runge_kutta = []
    xx = []

    for i in range(1, int(n) - 1):
        xx.append(i)
        xs_e, ys_e = euler_method.computations(x0, y0, x, i)
        xs_ie, ys_ie = improved_euler_method.computations(x0, y0, x, i)
        xs_rk, ys_rk = runge_kutta_method.computations(x0, y0, x, i)
        xs_es, ys_es = exact_solution.computations(x0, y0, x, i)

        imax_error_euler = []
        imax_error_improved_euler = []
        imax_error_runge_kutta = []

        for j in range(i):
             imax_error_euler.append(abs(ys_es[j] - ys_e[j]))
             imax_error_improved_euler.append(abs(ys_es[j] - ys_ie[j]))
             imax_error_runge_kutta.append(abs(ys_es[j] - ys_rk[j]))

# find max error for given number of steps

        max_error_euler.append(max(imax_error_euler))
        max_error_improved_euler.append(max(imax_error_improved_euler))
        max_error_runge_kutta.append(max(imax_error_runge_kutta))

    errors = [xx, max_error_euler, max_error_improved_euler, max_error_runge_kutta]
    return errors


