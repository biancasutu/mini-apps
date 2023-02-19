FILEPATH = 'to_do_app/todos.txt'
# pt a crea executabilul, FILEPATH trebuie sa fie = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list 
    of to-do items
    This text is called --doc (documentation) strings-- 
    It prints the text(documentation) when you write
    help(function) in console
    """
    with open(filepath, 'r') as f:
        todos_local  = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)

print(__name__)

if __name__ == '__main__':
    print('Hello from functions module')
    print(get_todos())

# print(__name__) afiseaza __main__ in fisierul.py unde 
# exista secventa if name == main, iar in alt fisier.py unde a 
# fost importat functions va afisa numele fisierului.py (functions)

# ce se afla in secventa if __name__ == "__main__" va fi rulat doar 
# atunci cand functions.py este executat direct, nu si atunci cand
# este importat in alt fisier.py