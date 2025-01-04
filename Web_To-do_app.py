import streamlit as st
import function as fs

todos = fs.get_todos()

st.title("My Todo App")
st.subheader('This is my todo app.')
st.write('This app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fs.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="INPUT_BOX", label_visibility="hidden"
              , placeholder="Add new todo..."
              , key="ADD_TODO"
              , on_change=fs.add_todo)
