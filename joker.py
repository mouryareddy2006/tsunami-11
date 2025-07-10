import streamlit as st
st.title("MOURYA'S FIRST PROJECT ON CODING")
st.header("welcome")
st.write("this is a basic website which i have made using python")

name=st.text_input("enter your name:")
if name:
   st.success(f"hello,{name}! how are you?,My name is MOURYA how can i help u My name is Mourya. Im currently pursuing my B.Tech and Im from Hyderabad,I have a strong interest in coding and Im always eager to learn new things in the world of technology. Thats one of the reasons Im here — Im looking forward to getting some coding tasks and challenges to improve my skill Im excited to connect with people who share similar interests and grow together")




number=st.slider("pick your age",0,100)
st.write(f"your age is {number}")


