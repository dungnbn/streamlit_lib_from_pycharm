"""
- basic create and connect streamlit with github: https://www.youtube.com/watch?v=IVhskhyjXNY
- connect pycharm project to github: https://www.youtube.com/watch?v=cOBv4HFfS-M&t=107s

- streamlit icons: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
"""

import streamlit as st
import time

# https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config
st.set_page_config(
    page_title="Cool App",
    # page_icon="😊",           # can either add an icon
    # page_icon=":joy:"
    page_icon="smile.png",      # or an image
    layout="centered",              # align everything to "centered" (default), or "wide" to fit the web's width
    initial_sidebar_state="expanded" # setting the behaviour of sidebar (st.sidebar) if exists
)

st.title("Streamlit Test")

st.sidebar.title("Sidebar")

with st.sidebar:
    st.write("1. Item 1")
    st.write("2. Item 2")

with st.expander("Hidden text"):
    st.write("hello", 10)
    st.write(":grin:")
    st.write(5)

# https://docs.streamlit.io/develop/api-reference/layout/st.columns
# https://www.youtube.com/watch?v=kTZg48MQ-t0
col1, col2, col3 = st.columns(3)

with col1:
    st.header("JavaScript")
    st.image("javascript.png")
    st.link_button("JavaScript", "https://www.javascript.com/")

with col2:
    st.header("Python")
    st.image("python.png")
    st.link_button("Python", "https://www.python.org/")

with col3:
    st.header("Java")
    st.image("java.png")
    st.link_button("Java", "https://www.java.com/en/")


check_box = st.checkbox("I confirm")
button = st.button("Submit")
if check_box and button:
    my_bar = st.progress(0.0, "wow")
    for per in range(11):
        time.sleep(0.05)
        my_bar.progress(per/10)
    st.balloons()

