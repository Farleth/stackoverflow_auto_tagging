import streamlit as st
from api import post_data
import requests
import os
from dotenv import load_dotenv

st.set_page_config(layout="wide")

load_dotenv()

api = os.getenv("API_URL")

st.title("Stackoverflow auto taggingz")
st.write("by Moixim, EliBuisness et Empereur canard")

col1, col2 = st.columns(2)

with col1:
    title = st.text_input("Titre")
    post = st.text_area("Post")
    All = title + " - " + post

    pred = requests.get(f'{api}{All}').content

with col2:
    st.title("Predictions")
    st.write(f"recommended tags are: {str(pred)}")

if st.button("Save Model Prediction"):
    post_data(title, post, pred)
