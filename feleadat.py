import streamlit as st

st.header("Kerdoív") 


st.text("Kerdoiv!!!")

name = st.text_input("Enter Your name", "Type Here ...")

if(st.button('Submit')):
	result = name.title()
	st.success(result)
email = st.text_input("Enter your email", "Type Here")
level = st.slider("Select your age", 1, 99)
gender = st.radio("Select Gender: ", ('Male', 'Female'))


