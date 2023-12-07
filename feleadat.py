import streamlit as st

st.header("Kerdoív") 


st.text("Kerdoiv!!!")

name = st.text_input("Enter Your name", "Type Here ...")
email = st.text_input("Enter your email", "Type Here ...")
kor= st.text_input("Enter your age", "Type Here ...")
gender = st.radio("Select Gender: ", ('Male', 'Female'))

name = st.text_input(".text_input: Enter Your name", "Type Here ...")

if(st.button('.button: Submit')):
	result = name.title()
	st.success(result)
