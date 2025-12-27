import streamlit as st

st.title('My Streamlit App')
st.write('Welcome! This app')

st.header("Select a number")
number = st.slider("Pick number", 0, 100, 5)

st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**")