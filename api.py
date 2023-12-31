import pandas as pd
import pickle
from supabase import create_client, Client
from nltk.corpus import stopwords
import pandas as pd
import nltk
import re
import mlflow
from fastapi import FastAPI
import uvicorn
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

import requests

# Initialize FastAPI app
app = FastAPI()

url = "https://bosbinvsnempbohyiwjy.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvc2JpbnZzbmVtcGJvaHlpd2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMwNjY2OTQsImV4cCI6MjAxODY0MjY5NH0.1_2dP0dRw2tSiEjervRFTXWftM77DbTk3IHyT6C1Rcc"
supabase: Client = create_client(url, key)

def train_model():
    data = get_data()
    X=data.clean_text
    y=data['Tfidf Clus Label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

    nb = Pipeline([('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', MultinomialNB()),
                ])
    nb.fit(X_train, y_train)
    return nb

def get_data():
    response = supabase.from_('data').select('*').execute()
    df = pd.DataFrame(response.data)

def post_data(title, body, pred):
    data, count = supabase.table('data').insert({"Title": title, "Body": body, "Tags": str(pred)}).execute()
    print("Posting data response ", data, count)

def cleanhtml(sentence): #function to clean the word of any html-tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', sentence)
    return cleantext

def cleanpunc(sentence): #function to clean the word of any punctuation or special characters
    cleaned = re.sub(r'[?|!|\'|"|#]',r'',sentence)
    cleaned = re.sub(r'[.|,|)|(|\|/]',r' ',cleaned)
    return  cleaned

def stem(text: str):
    sno = nltk.stem.SnowballStemmer('english') #initialising the snowball stemmer which is developed in recent years
    stop=set(stopwords.words('english'))

    str1=' '
    final_string=[]
    s=''

    filtered_sentence=[]
    #print(sent);
    sent=cleanhtml(text) # remove HTMl tags
    for w in sent.split():
        for cleaned_words in cleanpunc(w).split():
            if((cleaned_words.isalpha()) & (len(cleaned_words)>2)):
                if(cleaned_words.lower() not in stop):
                    s=(sno.stem(cleaned_words.lower())).encode('utf8')
                    filtered_sentence.append(s)
                else:
                    continue
            else:
                continue
    #print(filtered_sentence)
    str1 = b" ".join(filtered_sentence) #final string of cleaned words
    #print("***********************************************************************")

    final_string.append(str1)

    return pd.Series(final_string[0].decode('utf8'))

pickled_model = pickle.load(open('notebooks/supervised.pkl', 'rb'))


@app.get("/predict_tag")
def predict(All: str, model):

    pred = model.predict(stem(All))
    convert = ["imag, button, text, view, color, page, use, click, css, element", "string, convert, charact, format, use, return, valu, like, split, way", "tabl, column, sql, select, datafram, date, databas, queri, row, data", "android, gradl, com, studio, build, app, project, googl, apk, use", "instal, packag, npm, python, usr, pip, version, gem, run, command", "file, line, directori, use, project, path, folder, command, get, tri", "array, numpi, object, element, function, valu, int, use, list, loop", "class, public, int, return, method, object, static, void, type, privat", "request, server, http, web, api, net, use, json, post, respons", "use, differ, code, function, like, get, run, way, would, test"]
    pred = convert[pred[0]]

    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")

        # Save the MLflow run ID for reference
        run_id = mlflow.active_run().info.run_id

        # Log additional information
        mlflow.log_param("prediction", pred)


    return pred

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
