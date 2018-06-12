import command_system
import json
import os

def emote(arg):
    message = "no suitable emotuions as " + arg + " founded"
    attachment=""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "images.json")
    with open(json_url) as f:
        data = json.load(f)
    for i in data:
        cur = data.get(i)
        if cur['code'] == arg:
            message=""
            attachment = 'http://static-cdn.jtvnw.net/emoticons/v1/' + str(data.get(i)['id']) + '/3.0'
            break
    return message, attachment

emote_command = command_system.Command()

emote_command.keys = ['emote']
emote_command.description = 'Кину emote с twitch.tv'
emote_command.process = emote
