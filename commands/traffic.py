import command_system
import json
import os

def traffic(arg):
    attachment="https://static-maps.yandex.ru/1.x/?ll=43.966391,56.285877&spn=0.1,0.1&l=map,trf&size=650,450"
    return message, attachment

traffic_command = command_system.Command()

traffic.keys = ['пробки', 'jam', 'traffic', 'карта']
traffic.description = 'Кину карту с пробками на данный момент'
traffic.process = traffic



https://static-maps.yandex.ru/1.x/?ll=43.966391,56.285877&spn=0.1,0.1&l=map,trf&size=650,450