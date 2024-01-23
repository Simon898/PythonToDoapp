FPath = 'todos.txt'


def get_todos(filepath=FPath):
    """Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file:
        todos_loc = file.readlines()
    return todos_loc


def write_todos(todos_loc,filepath=FPath):
    """Write to-do items list in the text file."""
    with open("todos.txt", "w") as file:
        file.writelines(todos_loc)
