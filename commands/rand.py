import random
import command_system

def rand(arg):
    space_pos = arg.find(' ');
    x = arg[:space_pos]
    y = arg[space_pos+1:]
    message = 'Рандом от ' + x + ' до ' + y + ':\n'
    try:
        x = int(x)
        y = int(y)
        rand_res = random.randint(x, y)
        message += str(rand_res)
    except:
        message = "Ошибка вызова. Использование: рандом x y. (рандом 0 100)"
    return message, ""

rand_command = command_system.Command()

rand_command.keys = ['рандом', 'randint', 'random']
rand_command.description = 'Выберу рандомное число из диапазона [x:y]. Использование: рандом x y'
rand_command.process = rand