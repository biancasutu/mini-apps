from functions import get_todos, write_todos
import time

now = time.strftime("%b %m, %Y %H:%M:%S")
print("It is ", now)
 
while True:
    user_action = input('Type add, show, edit, complete or exit: ').lower()
    user_action = user_action.strip()   # for the case when the user types accidentally "add "

    # match user_action:
        # case 'add':
    if user_action.startswith('add'): 
        todo = user_action[4:].capitalize()

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    # case 'show' | 'display':   # user can choose both commands, both doing the same thing
    elif user_action.startswith('show'):

        todos = get_todos('to_do_app/todos.txt') 

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index + 1} - {item}')

    # case 'edit':
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) 
            number = number - 1

            todos = get_todos()

            new_todo = input('Edit chosen to do: ')
            todos[number] = new_todo + '\n'
 
            write_todos(todos)

        except IndexError:
            print("You don't have so many tasks.")
            continue
        except ValueError:
            print('Your command is not valid.')
            continue   # ignores all the code below and goes directly to the start of the while loop


    # case 'complete':
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos()

            print(f'Todo {todo_to_remove} was removed from the list.')
        except IndexError:
            print("You don't have so many tasks.")
            continue

    # case 'exit':
    elif user_action.startswith('exit'):
        break

    else:
        print('Command is not valid!')

    # case _:
    #     print('You entered an unknown command')
    # # the last case is covering the possibility when user types anything other then the above commands


print('Bye!')

# file = open(r"C:\Users\downloads\todos.txt", 'r')  - absolute path, for files outside of the project
# r"path" = row string - ignores special characters