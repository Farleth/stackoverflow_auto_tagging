import streamlit as st


st.title("Stackoverflow auto tagging")
st.write("by Moixim, EliBuisness et Empereur canard")

col1,col2 = st.columns(2)

with col1:
    title = st.text_input("Titre")
    post = st.text_area("Post")
    All = title + " - " + post


with col2:
    pass
