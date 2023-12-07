import streamlit as st

st.header("Kerdoív") 


st.text("Kerdoiv!!!")

name = st.text_input("Enter Your name", "Type Here ...")
email = st.text_input("Enter your email", "Type Here ...")
kor= st.text_input("Írd be a korord", "Type Here ...")
gender = st.radio("Select Gender: ", ('Male', 'Female'))
