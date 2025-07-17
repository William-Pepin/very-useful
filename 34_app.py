import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(5,3),
    columns=['a','b','c'])

st.title("Random Table")
st.write(df)
st.title("Random Chart")
st.line_chart(df)