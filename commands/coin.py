import random
import command_system


def coin(arg):
   # Бросаем монетку
    message = 'Бросаем монетку:\n'
    flip = random.randint(0, 1)
    if (flip == 0):
        message += 'Решка'
    else:
        message += 'Орел'
    return message, ""

coin_command = command_system.Command()

coin_command.keys = ['монетка', 'монета', 'орел', 'решка', 'коин', 'flip', 'coin']
coin_command.description = 'Подброшу монетку'
coin_command.process = coin