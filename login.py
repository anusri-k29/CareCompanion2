import streamlit as st

def login_page():
    st.title("🔐 Login to Care Companion")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with real authentication
            st.session_state["logged_in"] = True
            st.success("✅ Login successful! Redirecting...")
            st.rerun()
        else:
            st.error("❌ Invalid username or password")

    if st.session_state["logged_in"]:
        st.success("✅ You are logged in!")
