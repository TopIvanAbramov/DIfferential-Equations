import PySimpleGUI as sg
from Generate_graphs import generate_solution_graphs, generate_errors_graphs, generate_error_analysis_graphs, clear_graph
import seaborn as sns

# Initialize interface

sns.set()
image_elem = sg.Image(filename='solution.png')

layout = [[sg.Text('Enter initial values:', font='San\ Francisco 15')],
      [sg.Text('X0', size=(8, 1), justification='center'), sg.Text('Y0', size=(11, 1), justification='center'), sg.Text('X', size=(7, 1), justification='center')],
      [
          sg.InputText(size=(8,1), key='x0'),
          sg.InputText(size=(8,1), key='y0'),
          sg.InputText(size=(8,1), key='x'),
       ],
      [sg.Text('')],
      [sg.Text("N", size=(30, 1), justification='center')],
      [sg.Slider(range=(10, 1000),
                     default_value=100,
                     size=(32, 15),
                     orientation='horizontal', key='n')],
      [sg.Text('')],
      [
          sg.Button('Solution', font='San\ Francisco 15'),
          sg.Button('Solution errors', font='San\ Francisco 15'),
          sg.Button('Error analysis', font='San\ Francisco 15'),
          sg.Button('Clear')
      ],
      [sg.Text('', key="error", size=(25, 1))],
      [sg.Image('Graphs/solution.png', key='graph')],
      ]


clear_graph.clear()

window = sg.Window("Solve initial value problem for: y' = 1 + 2y/x", size=(680, 760), font='San\ Francisco 15').Layout(layout)

# Event loop

while True:
    button, values = window.Read()

    if button is None:
        break
    else:
        x0 = y0 = x = n = 0
        try:
            x0 = float(values['x0'])
            y0 = float(values['y0'])
            x = float(values['x'])
            n = float(values['n'])
            window.FindElement('error').Update(" ")
        except:
            window.FindElement('error').Update("Please, enter valid numbers")
            continue

#Handle button pushes

    if button == "Solution":
        generate_solution_graphs.solution_graphs(x0, y0, x, n)
        window.FindElement('graph').Update('Graphs/solution.png')

    if button == "Solution errors":
        generate_errors_graphs.error_graphs(x0, y0, x, n)
        window.FindElement('graph').Update('Graphs/solution_error.png')


    if button == "Error analysis":
        generate_error_analysis_graphs.error_analysis_graphs(x0, y0, x, n)
        window.FindElement('graph').Update('Graphs/error_analysis.png')

    if button == "Clear":
        clear_graph.clear()
        window.FindElement('graph').Update('Graphs/solution.png')
