import function
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("TealMono")

label_clock = sg.Text('', key='clock')
label = sg.Text('Type in todo!')
input_label = sg.InputText(tooltip="Enter todo: ", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      enable_events=True, size=(45,10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window('My todo app!',
                   layout=[[label_clock],
                           [label],
                           [input_label, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Arial', 16))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(values)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Select todo to be edited first!', font=('Arial', 16))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Select todo to be edited first!', font=('Arial', 16))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
