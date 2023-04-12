FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as files:
        todos_local = files.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())
