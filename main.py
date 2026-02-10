"""
- basic create and connect streamlit with github: https://www.youtube.com/watch?v=IVhskhyjXNY

"""

import streamlit as st
import time


st.write("hello", 10)
st.write(":grin:")
st.write(5)

my_bar = st.progress(10, "wow")
for per in range(90):
    time.sleep(0.05)
    my_bar.progress(per + 10)

if st.button("click"):
    st.balloons()
