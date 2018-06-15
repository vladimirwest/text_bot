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
    get_weather_info = False
    day_counter = 0
    current_date = ""
    cleared = False
    temp_Log = ""
    Log = ""
    for weather in f:
        
        print(weather.get_reference_time('date'))
        if ( (arg == "завтра") and (day_counter == 1) and (not cleared)):
            Log = ""
            cleared = True
           
        if(current_date != str(weather.get_reference_time('date').date()).split('-')[2]):
            temp_Log = temp_Log + (str(weather.get_reference_time('date').date()).split('-')[2] + " " + months[str(weather.get_reference_time('date').date()).split('-')[1]] + ":\n")
            current_date = str(weather.get_reference_time('date').date()).split('-')[2]
        
        if (str(weather.get_reference_time('date').time()).split(':')[0] == "09"):
            temp_Log = temp_Log + ("\t🌝 Утро: ")
            get_weather_info = True
 
        if (str(weather.get_reference_time('date').time()).split(':')[0] == "15"):
            temp_Log = temp_Log + ("\t🌞 День: ")
            get_weather_info = True
                
        if (str(weather.get_reference_time('date').time()).split(':')[0] == "21"):
            temp_Log = temp_Log + ("\t🌛 Вечер: ")
            get_weather_info = True
            day_counter = day_counter + 1
 
        if (str(weather.get_reference_time('date').time()).split(':')[0] == "03"):
            temp_Log = temp_Log + ("\t🌚 Ночь: ")
            get_weather_info = True
 
        if (get_weather_info):   
            wind = "{0} {1}".format(weather.get_wind()['speed'], winddirArray[int(math.floor(weather.get_wind()['deg'] + 0.5) % 16)])
            humidity = weather.get_humidity()
            temp = weather.get_temperature('celsius')['temp']
            status = weather.get_status()
            try:
                weatherResult = "{0}°C {1} {2}, wind {3} m/s, humidity {4}%".format(temp, status,emojisDict[status], wind, humidity)
                temp_Log = temp_Log + weatherResult + "\n"
            except TypeError:
                weatherResult = "{0}°C {1}, wind {2} m/s, humidity {3}%".format(temp, status, wind,humidity)
                temp_Log = temp_Log + weatherResult + "\n"
           
            if (str(weather.get_reference_time('date').time()).split(':')[0] == "21"):
                Log = Log + temp_Log
                temp_Log = ""
           
            if ( (arg == "сегодня" or arg == "") and day_counter == 1):
                return Log,""
 
            if (arg == "завтра" and day_counter == 2):
                return Log,""
            get_weather_info = False
 

    if(arg == "прогноз"):
        return Log,""
 
 
weather_command = command_system.Command()
 
weather_command.keys = ['погода', 'weather']
weather_command.description = 'Выведу текущую погоду в Нижнем Новгороде'
weather_command.process = weather