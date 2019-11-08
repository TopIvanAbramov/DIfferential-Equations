from Methods import euler_method, exact_solution, improved_euler_method, runge_kutta_method
import matplotlib.pyplot as plt
import os

def solution_graphs(x0, y0, x, n): #function generate graphs of solutions for DE
    xs_euler, ys_euler = euler_method.computations(x0, y0, x, n)
    xs_improved_euler, ys_improved_euler = improved_euler_method.computations(x0, y0, x, n)
    xs_runge_kutta, ys_runge_kutta = runge_kutta_method.computations(x0, y0, x, n)
    xs_exact, ys_exact = exact_solution.computations(x0, y0, x, n)

    plt.close()
    plt.plot(xs_exact, ys_exact, label='Exact solution')
    plt.plot(xs_euler, ys_euler, label='Euler method solution')
    plt.plot(xs_improved_euler, ys_improved_euler, label='Improved Euler method solution')
    plt.plot(xs_runge_kutta, ys_runge_kutta, label='Runge Kutta method solution')
    # plt.legend(loc=0)
    plt.legend(
        ("Exact solution", "Euler method solution", "Improved Euler method solution", "Runge Kutta method solution "),
        frameon=False)

    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/Graphs/solution.png")