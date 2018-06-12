import pyowm
import math
import command_system
from settings import *

def weather(arg):
    data = pyowm.OWM(WeatherAPIKey).weather_at_place('Nizhny Novgorod,ru').get_weather()
    winddirArray = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
    emojisDict = {'Clear':'☀','Clouds':'☁','Rain':'☂','Snow':'☃'}
    wind = "{0} {1}".format(data.get_wind()['speed'], winddirArray[int(math.floor(data.get_wind()['deg'] + 0.5) % 16)])
    humidity = data.get_humidity()
    temp = data.get_temperature('celsius')['temp']
    status = data.get_status()
    try:
        weatherResult = "{0}°C {1} {2}, wind {3} m/s, humidity {4}%".format(temp, status,emojisDict[status], wind, humidity)
    except TypeError:
        weatherResult = "{0}°C {1}, wind {2} m/s, humidity {3}%".format(temp, status, wind,humidity)
    return weatherResult, ""

weather_command = command_system.Command()

weather_command.keys = ['погода', 'weather']
weather_command.description = 'Выведу текущую погоду в Нижнем Новгороде'
weather_command.process = weather