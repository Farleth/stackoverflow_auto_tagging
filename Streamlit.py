import streamlit as st
import pickle
from api import get_data, post_data, stem
import pandas as pd
import numpy as np

import mlflow
st.set_page_config(layout="wide")

pickled_model = pickle.load(open('notebooks/supervised.pkl', 'rb'))

st.title("Stackoverflow auto taggingz")
st.write("by Moixim, EliBuisness et Empereur canard")

col1, col2 = st.columns(2)

with col1:
    title = st.text_input("Titre")
    post = st.text_area("Post")
    All = title + " - " + post

pred = pickled_model.predict(stem(All))
convert = ["imag, button, text, view, color, page, use, click, css, element", "string, convert, charact, format, use, return, valu, like, split, way", "tabl, column, sql, select, datafram, date, databas, queri, row, data", "android, gradl, com, studio, build, app, project, googl, apk, use", "instal, packag, npm, python, usr, pip, version, gem, run, command", "file, line, directori, use, project, path, folder, command, get, tri", "array, numpi, object, element, function, valu, int, use, list, loop", "class, public, int, return, method, object, static, void, type, privat", "request, server, http, web, api, net, use, json, post, respons", "use, differ, code, function, like, get, run, way, would, test"]
pred = convert[pred[0]]


with col2:
    st.title("Predictions")
    st.write(pred)

if st.button("Save Model Prediction"):
    post_data(title, post, pred)
