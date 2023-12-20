from stackapi import StackAPI
import pandas as pd

SITE = StackAPI('stackoverflow')
posts = SITE.fetch('questions', filter="withbody")
print(posts)

items = posts.get("items")

title_list = []
body_list = []

for i in items:
    title = i.get('title')
    body = i.get('body')
    title_list.append(title)
    body_list.append(body)


df = pd.DataFrame(data=[title_list, body_list], columns=['title', 'body'])

print(df)
