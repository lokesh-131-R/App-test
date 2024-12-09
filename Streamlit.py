import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def authenticate(username, password):
    # Replace these with your desired username and password
    return username == "username" and password == "password"
  
st.write("Hello World")
