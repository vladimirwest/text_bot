import random
import command_system


def coin(arg):
   # ������� �������
    message = '������� �������:\n'
    flip = random.randint(0, 1)
    if (flip == 0):
        message += '�����'
    else:
        message += '����'
    return message, ""

coin_command = command_system.Command()

coin_command.keys = ['�������', '������', '����', '�����', '����', 'flip', 'coin']
coin_command.description = '�������� �������'
coin_command.process = coin