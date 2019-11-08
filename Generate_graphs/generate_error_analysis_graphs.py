from Error_analysis.error_analysis import analysis
import matplotlib.pyplot as plt
import os

def error_analysis_graphs(x0, y0, x, n): #function generate graphs of global errors for DE

    xx, max_error_euler, max_error_improved_euler, max_error_runge_kutta = analysis(x0, y0, x, n)
    plt.close()
    plt.plot(xx, max_error_euler, xx, max_error_improved_euler, xx, max_error_runge_kutta)
    plt.legend(("Euler method max error", "Improved Euler method max error", "Rudge Kutta method max error"),
               frameon=False)
    plt.xlabel(r'$n$')
    plt.ylabel(r'$y$')
    plt.grid(True)
    plt.savefig(os.getcwd() + "/Graphs/error_analysis.png")