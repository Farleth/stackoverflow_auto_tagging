import streamlit as st
import pickle
from api import get_data, post_data
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

pred = pickled_model.predict(pd.Series(All))

with col2:
    st.write(pred)

with st.button("Save Model Prediction"):
    st.write(title, " -> ", type(title))
    st.write(post, " -> ", type(post))
    st.write(pred, " -> ", type(pred))
    post_data(title, post, pred[0])
