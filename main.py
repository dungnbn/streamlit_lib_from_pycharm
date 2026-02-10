"""
- basic create and connect streamlit with github: https://www.youtube.com/watch?v=IVhskhyjXNY
- connect pycharm project to github: https://www.youtube.com/watch?v=cOBv4HFfS-M&t=107s
"""

import streamlit as st
import time

st.title("Streamlit Test")

st.write("hello", 10)
st.write(":grin:")
st.write(5)

my_bar = st.progress(10, "wow")
for per in range(90):
    time.sleep(0.01)
    my_bar.progress(per + 10)

check_box = st.checkbox("I confirm")
button = st.button("Submit")
if check_box and button:
    st.balloons()

