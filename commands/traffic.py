import command_system

def traffic(arg):
    arg=arg.lower()
    if(arg=="сормовский" or arg=="сормово"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.890148%2C56.334155&spn=0.05,0.05&l=map,trf&size=650,450'
    elif(arg=="московский"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.918577%2C56.328852&spn=0.03,0.03&l=map,trf&size=650,450'
    elif(arg == "нижегородский"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=44.001746%2C56.316205&spn=0.05,0.05&l=map,trf&size=650,450'
    elif(arg == "центр"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=44.001746%2C56.316205&spn=0.03,0.03&l=map,trf&size=650,450'
    elif(arg=="автозаводский" or arg=="автозавод"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.901386%2C56.257318&spn=0.05,0.05&l=map,trf&size=650,450'
    elif(arg=="советский"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=44.025558%2C56.266703&spn=0.05,0.05&l=map,trf&size=650,450'
    elif(arg=="канавинский" or arg == "ленинский"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.900768%2C56.298704&spn=0.05,0.05&l=map,trf&size=650,450'
    elif(arg=="приокский"):
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.988814%2C56.252447&spn=0.05,0.05&l=map,trf&size=650,450'
    else:
        arg=""
        attachment = 'https://static-maps.yandex.ru/1.x/?ll=43.966391,56.285877&spn=0.1,0.1&l=map,trf&size=650,450'
    message = "Текущая ситуация на дорогах " + arg + ":"
    return message, attachment

traffic_command = command_system.Command()

traffic_command.keys = ['пробки', 'traffic', 'jam', 'карта', 'дороги']
traffic_command.description = 'Кину карту с пробками в Нижнем на данный момент. Для поиска по району добавьте название района после ключевого слова. (например, пробки ленинский)'
traffic_command.process = traffic