from stackapi import StackAPI
import pandas as pd
import os
from supabase import create_client, Client

url = "https://bosbinvsnempbohyiwjy.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvc2JpbnZzbmVtcGJvaHlpd2p5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDMwNjY2OTQsImV4cCI6MjAxODY0MjY5NH0.1_2dP0dRw2tSiEjervRFTXWftM77DbTk3IHyT6C1Rcc"
supabase: Client = create_client(url, key)

def get_data():
    response = supabase.from_('data').select('*').execute()
    df = pd.DataFrame(response.data)

def post_data(title, body, pred):
    data, count = supabase.table('data').insert(json={"id": 100000, "Title": title, "Body": body, "Tags": pred}).execute()
    print("Posting data response ", data, count)
