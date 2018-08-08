import json
import urllib.request
from urllib.error import HTTPError


#Reading json with Twitch global emotes
url_address ='https://twitchemotes.com/api_cache/v3/global.json'
with urllib.request.urlopen(url_address) as url:
    global_emotes = json.loads(url.read())
    
#Reading json with Twitch subscribers emotes    
url_addresss ='https://twitchemotes.com/api_cache/v3/subscriber.json'
with urllib.request.urlopen(url_addresss) as url:
    subscriber_emotes = json.loads(url.read())

#Creating a dict to store only the {'emote_code':'emote_id'} to optimize the search.
emotes = dict()
for emote in global_emotes:
    emotes[global_emotes.get(emote).get('code')] = global_emotes.get(emote).get('id')
for item in subscriber_emotes:
    for emote_list in range(len(subscriber_emotes.get(item).get('emotes'))):
           emotes[subscriber_emotes.get(item).get('emotes')[emote_list].get('code')] = subscriber_emotes.get(item).get('emotes')[emote_list].get('id')

#Writing to your home directory. Dont forget to change the path to your liking.
with open('Emote_codes.json', 'w') as outfile:
    json.dump(emotes, outfile)
        