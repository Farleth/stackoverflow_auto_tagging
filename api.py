from stackapi import StackAPI
import pandas as pd
import os
from supabase import create_client, Client
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from sklearn import metrics
import matplotlib.cm as cm
import pandas as pd
import numpy as np
import random
import nltk
import re
import mlflow

url = "https://bosbinvsnempbohyiwjy.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvc2JpbnZzbmVtcGJvaHlpd2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMwNjY2OTQsImV4cCI6MjAxODY0MjY5NH0.1_2dP0dRw2tSiEjervRFTXWftM77DbTk3IHyT6C1Rcc"
supabase: Client = create_client(url, key)

def get_data():
    response = supabase.from_('data').select('*').execute()
    df = pd.DataFrame(response.data)

def post_data(title, body, pred):
    data, count, a = supabase.table('data').insert({"Title": title, "Body": body, "Tags": str(pred)}).execute()
    print("Posting data response ", data, count, a)

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
