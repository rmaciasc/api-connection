import praw
import json
import pandas as pd

with open('./credentials.json') as f:
    params = json.load(f)

red = praw.Reddit(client_id= params['client_id'],
                  client_secret= params['client_secret'],
                  password= params['password'],
                  username= params['username'],
                  user_agent= params['user_agent'])

print(red.user.me()) # Verificamos que nos hayamos conectado

top_dict = {
    "title": [],
    "score": [],
    "id": [],
    "comm_num": [],
    "created": [],
    "body": [],
    "url": []
} #Creamos un diccionario para guardar todo lo que nos interese

subreddit = red.subreddit('mechanicalkeyboards')
print(subreddit.subscribers)
top_subreddit = subreddit.hot(limit=11)
dir(subreddit)


for post in top_subreddit:
    top_dict['title'].append(post.title)
    top_dict['score'].append(post.score)
    top_dict['id'].append(post.id)
    top_dict['comm_num'].append(post.num_comments)
    top_dict['body'].append(post.selftext)
    top_dict['created'].append(post.created)
    top_dict['url'].append(post.comments)
    #top_dict['url'].append(post.permalink)

top_dict = {d: top_dict[d][1:] for d in top_dict}

dftop = pd.DataFrame(top_dict)
dftop['date'] = pd.to_datetime(dftop.created, unit='s')
print(dftop)
dftop.to_csv('./hot posts MK.csv', index=False)