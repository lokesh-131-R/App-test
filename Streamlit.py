import streamlit as st

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Authentication function
def authenticate(username, password):
    # Replace these with your desired username and password
    return username == "username" and password == "password"

# Authentication flow
if not st.session_state["authenticated"]:
    st.title("Login")
    
    # Create input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Button to submit login
    if st.button("Login"):
        if authenticate(username, password):
            st.session_state["authenticated"] = True
            st.success("Login successful!")
            # Add a rerun to immediately refresh the interface
            st.experimental_set_query_params()  # Safe way to trigger rerun
        else:
            st.error("Invalid username or password.")
else:
    st.title("Welcome!")
    st.write("Hello World")
    
    # Logout button
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.experimental_set_query_params()  # Safe way to trigger rerun

