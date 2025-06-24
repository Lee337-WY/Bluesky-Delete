from atproto import Client
from datetime import datetime, timedelta
import os

user = os.environ.get('BS_USER', None)
pw = os.environ.get('BS_PW', None)

client = Client()
client.login(user,pw)

response = client.get_author_feed(user)

print('Posts='+str(len(response.feed))+'\n')

for idx in range(len(response.feed)):
    print('Post '+str(idx))
    print(response.feed[idx].post.indexed_at)
    print(response.feed[idx].post.record.text)

    elapsed=datetime.now()-datetime.strptime(response.feed[idx].post.indexed_at[0:19],'%Y-%m-%dT%H:%M:%S')

    if elapsed > timedelta(hours=48):
        print('DELETE ', client.delete_post(response.feed[idx].post.uri))

    print('')
