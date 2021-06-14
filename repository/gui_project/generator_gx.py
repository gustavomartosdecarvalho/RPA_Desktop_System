import PySimpleGUI as sg
import random
import time

# Tkinter don't work in a virtualenv

sg.theme('TanBlue')
layout = [  [sg.Text('Set initial System:    '), sg.InputText(key='-INIT-', size = (4, 4))],
            [sg.Text('Number of the Process: '), sg.InputText(key='-PROC-', size = (4, 4))],
            [sg.Button('Show'), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'Show':
        sg.popup("Completed system: " + str(values['-INIT-']),
         "Number Process:" + str( values['-PROC-']),
         "We find " + str(random.randrange(3, 9124)) + " files")

window.close()