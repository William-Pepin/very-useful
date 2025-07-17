import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


df2 = pd.DataFrame(np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

st.title("Blue dots")

c = alt.Chart(df2).mark_circle().encode(x='a',y='b',size='c',color='c',tooltip=['a','b','c'])
st.write(c)

st.text('OH WOW, LET ME TELL YOU — I ABSOLUTELY ADORE BLUE DOTS!!! 💙💙 There’s just something MAGICAL about those tiny, perfect bursts of color that instantly brighten up everything around them. Whether they’re scattered playfully or lined up just right, blue dots are like little jewels of happiness dancing in my eyes! I CAN’T GET ENOUGH of their cool, calming vibe mixed with an electrifying pop of energy. Honestly, blue dots make my heart skip a beat — they’re simply UNBEATABLE!')