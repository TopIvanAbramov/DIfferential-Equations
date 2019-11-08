from Methods import euler_method, exact_solution, improved_euler_method, runge_kutta_method
import matplotlib.pyplot as plt
import os

def error_graphs(x0, y0, x, n): #function generate graphs of local errors for DE
    xs_euler, ys_euler = euler_method.computations(x0, y0, x, n)
    xs_improved_euler, ys_improved_euler = improved_euler_method.computations(x0, y0, x, n)
    xs_runge_kutta, ys_runge_kutta = runge_kutta_method.computations(x0, y0, x, n)
    xs_exact, ys_exact = exact_solution.computations(x0, y0, x, n)

    ys_error_euler = []
    for i in range(len(ys_euler) - 1):
        ys_error_euler.append(abs(ys_exact[i] - ys_euler[i]))

    ys_error_improved_euler = []
    for i in range(len(ys_improved_euler) - 1):
        ys_error_improved_euler.append(abs(ys_exact[i] - ys_improved_euler[i]))

    ys_error_runge_kutta = []
    for i in range(len(ys_runge_kutta) - 1):
        i += 1
        ys_error_runge_kutta.append(abs(ys_exact[i] - ys_runge_kutta[i]))

    if len(xs_euler) > len(ys_error_euler):
        xs_euler = xs_euler[:-1]

    if len(xs_euler) < len(ys_error_euler):
        ys_error_euler = ys_error_euler[:-1]

    if len(xs_improved_euler) > len(ys_error_improved_euler):
        xs_improved_euler = xs_improved_euler[:-1]

    if len(xs_improved_euler) < len(ys_error_improved_euler):
        ys_error_improved_euler = ys_error_improved_euler[:-1]

    if len(xs_runge_kutta) > len(ys_error_runge_kutta):
        xs_runge_kutta = xs_runge_kutta[:-1]

    if len(xs_runge_kutta) < len(ys_error_runge_kutta):
        ys_error_runge_kutta = ys_error_runge_kutta[:-1]

    plt.close()
    plt.plot(xs_euler, ys_error_euler, label='Euler method error')
    plt.plot(xs_improved_euler, ys_error_improved_euler, label='Improved euler method error')
    plt.plot(xs_runge_kutta, ys_error_runge_kutta, label='Runge Kutta method error')
    plt.legend(loc=0)

    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.legend(("Euler method error", "Improved Euler method error", "Rudge Kutta method error"), frameon=False)

    plt.savefig(os.getcwd() + "/Graphs/solution_error.png")