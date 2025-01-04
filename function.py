import streamlit as st

FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads a text file and return the items. """
    with open(filepath, 'r') as file_local:
         todos_local = file_local.readlines()
    return todos_local



def write_todos(todos_arg, filepath=FILEPATH):
    """" Writes text in the text file. """
    with open(filepath, 'w') as function_file:
        function_file.writelines(todos_arg)


def add_todo():
    new_todo = st.session_state["ADD_TODO"] + "\n"
    todos = get_todos()
    todos.append(new_todo)
    write_todos(todos)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())
