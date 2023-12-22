import streamlit as st
import pickle
from api import get_data, post_data, stem
import pandas as pd
import numpy as np

import mlflow

pickled_model = pickle.load(open('notebooks/supervised.pkl', 'rb'))

st.title("Stackoverflow auto taggingz")
st.write("by Moixim, EliBuisness et Empereur canard")

col1,col2 = st.columns(2)

with col1:
    title = st.text_input("Titre")
    post = st.text_area("Post")
    All = title + " - " + post

pred = pickled_model.predict(stem(All))

with col2:
    st.write(pred)

if st.button("Save Model Prediction"):
    post_data(title, post, pred[0])
