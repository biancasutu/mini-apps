import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file :
        pass

# Linii de comanda terminal:
# set-executionpolicy remotesigned -scope currentuser (dupa ce ruleaza se va inchide terminalul din 'local' si se va deschide din nou, trebuie sa apara venv)
# pip install pyinstaller -> se fol pt a crea executabile
# pyinstaller --onefile --windowed --clean gui.py (numele fisierului pe care vreau sa il fac .exe)

sg.theme('LightBlue2')

clock_label= sg.Text('', key='clock')
 
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", size=(36, 10),key="todo")
add_button = sg.Button("Add")
# add_button = sg.Button(size=10, image_source=r'to_do_app\images\add.png')  # pt a pune imagini pe butoane

list_box = sg.Listbox(values=functions.get_todos(), key='todos', 
                        enable_events=True, size=[40, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


window = sg.Window('My To-Do App',
                   layout=[[clock_label],
                   [label], 
                   [input_box, add_button], 
                   [list_box],
                   [edit_button, complete_button, exit_button]], 
                   font=('Helvetica', 15))  #this instance is stored in variable window

while True:
    event, values = window.read(timeout=900)  # timeout - pt a afisa ceasul tot timpul (nu doar cand userul alege un event)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            if not values['todo']:
                sg.popup('You must enter a task!', text_color='dark red', font=('Helvetica', 15))
            else:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a todo first!', text_color='dark red', font=('Helvetica', 15))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select a todo first!', text_color='dark red', font=('Helvetica', 15))
        case 'Exit':
            break
        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup('No task in the list!', text_color='dark red', font=('Helvetica', 15))
        case sg.WINDOW_CLOSED:
            break


window.close()