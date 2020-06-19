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

subreddit = red.subreddit('The_Donald')

ban_dict = {
    'user': [],
    'note': []
}
print(subreddit.subscribers)
for ban in subreddit.banned(): 
    ban_dict['user'].append(ban)
    ban_dict['note'].append(ban.note)

bandf = pd.DataFrame(ban_dict)
print(bandf)