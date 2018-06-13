import pyowm
import math
import command_system
from settings import *

months = {"01": "Января",  "02" : "Февраля", "03" : "Марта", "04" : "Апреля",
               "05" : "Мая", "06" : "Июня", "07" : "Июля", "08" : "Августа",
               "09" : "Сентября", "10" : "Октября", "11" : "Ноября", "12" : "Декабря"}
winddirArray = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
emojisDict = {'Clear':'☀','Clouds':'☁','Rain':'☂','Snow':'☃'}


def weather(arg):
    owm = pyowm.OWM(WeatherAPIKey)  # You MUST provide a valid API key
    fc = owm.three_hours_forecast('Nizhny Novgorod,ru')
    f = fc.get_forecast()
    skip_counter = 1
    day_time_counter = 1
    day_counter = 0
    Log = ""
    for weather in f:
        if (skip_counter%2 == 1):
            if (day_time_counter == 2):
                Log = Log + ("\t🌝 Утро: ")

            if (day_time_counter == 3):
                Log = Log + ("\t🌞 День: ")

            if (day_time_counter == 4):
                Log = Log + ("\t🌛 Вечер: ")
                day_time_counter = 0
                day_counter = day_counter + 1


            if (day_time_counter == 1):
                if ( (arg == "завтра") and day_counter == 1):
                    Log = ""
                Log = Log + (str(weather.get_reference_time('date').date()).split('-')[2] + " " + months[str(weather.get_reference_time('date').date()).split('-')[1]] + ":\n")
                Log = Log + ("\t🌚 Ночь: ")

            wind = "{0} {1}".format(weather.get_wind()['speed'], winddirArray[int(math.floor(weather.get_wind()['deg'] + 0.5) % 16)])
            humidity = weather.get_humidity()
            temp = weather.get_temperature('celsius')['temp']
            status = weather.get_status()
            try:
                weatherResult = "{0}°C {1} {2}, wind {3} m/s, humidity {4}%".format(temp, status,emojisDict[status], wind, humidity)
                Log = Log + weatherResult + "\n"
            except TypeError:
                weatherResult = "{0}°C {1}, wind {2} m/s, humidity {3}%".format(temp, status, wind,humidity)
                Log = Log + weatherResult + "\n"

            if ( (arg == "сегодня" or arg == "") and day_counter == 1):
                return Log,""

            if (arg == "завтра" and day_counter == 2):
                return Log,""

            day_time_counter = day_time_counter + 1

        skip_counter = skip_counter + 1
    if(arg == "прогноз"):
        return Log,""


weather_command = command_system.Command()

weather_command.keys = ['погода', 'weather']
weather_command.description = 'Выведу текущую погоду в Нижнем Новгороде'
weather_command.process = weather