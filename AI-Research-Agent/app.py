import streamlit as st

st.title("AI Research Agent")

query = st.text_input("Enter research topic")

if query:
    st.write("You searched for:", query)