import command_system
import json
import os

def emote(arg):
    scale = 2
    space_pos = arg.find(" ")
    if(space_pos!=-1):
        scale = arg[space_pos+1:]
        arg=arg[:space_pos]
        if(scale != str(1) and scale != str(3)):
            scale = 2
    message = "no suitable emotions as " + arg + " founded"
    attachment=""
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "Emote_codes.json")
    with open(json_url) as f:
        data = json.load(f)
        for i in data:
            if data[i] == arg:
                message=""
                attachment = 'http://static-cdn.jtvnw.net/emoticons/v1/' + str(i) + '/' + str(scale) + '.0'
                break
    return message, attachment

emote_command = command_system.Command()

emote_command.keys = ['emote']
emote_command.description = 'Кину emote с twitch.tv'
emote_command.process = emote
