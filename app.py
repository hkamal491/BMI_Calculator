import streamlit as st
st.title('BMI Calculator')
weight =st.number_input("Enter your weight in (Kg)")
height=st.number_input("Enter your Height in (m)")
if height >0:
    bmi=weight/(height**2)
    st.write(f"Your BMI is{bmi}")
    