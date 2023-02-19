import streamlit as st
import functions
import time

# streamlit run to_do_app/web.py
# streamlit = framework for data analytics and machine learning

todos = functions.get_todos()

def add_todo():     # this is a callback function
    todo = '\n' + st.session_state['new_todo']
    todos.append(todo)
    functions.write_todos(todos)


st.title('My Todo App')
# st.subheader('This is my todo app')
# st.write('This app is to increase your productivity')

st.subheader(time.strftime('%b %d, %Y %H:%M:%S'))

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # update in real time withot refreshing the webpage

st.text_input(label='', placeholder='Add a new todo...',
                on_change=add_todo, key='new_todo')

# st.session_state

# session_state is a very specific objet in streamlit, contains pair of data
# (looks like a dictionary), 
# shows the data added/edited in the web app only for the data tha t have a key, 
# helps when developing the app
# must be deleted before publishing the app for users



# for deploying your web app on cloud, you need to have in project 
# only the files used to develop the app + requirements.txt