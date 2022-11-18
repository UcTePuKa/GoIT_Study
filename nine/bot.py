import re


def input_error(func):
    def inner(*args, **kwargs):
        while True:
            try:
                func_res = func(*args, **kwargs)
                if func_res == -1:
                    break
            except KeyError:
                print('This contact doesnt exist, please try again.')
            except ValueError as exception:
                print('Wrong input. Please enter name "space" number')
            except IndexError:
                print('This contact cannot be added, it exists already')
            except TypeError:
                print('Unknown command or parametrs, please try again.')
    return inner

@input_error
def main():
    command = input('Please input the command: ')
    if re.findall(r'\.|exit|close|good.bye', command.lower()):
        print(exit_func())
        return -1
    elif re.findall(r'^hello', command.lower()):
        print(hello_func())
    elif re.findall(r'^help', command.lower()):
        print(help_func())
    elif re.findall(r'^add', command.lower()):
        print(add_func(command, contacts))
    elif re.findall(r'^change', command.lower()):
        print(change_func(command, contacts))
    elif re.findall(r'^phone', command.lower()):
        print(phone_func(command, contacts))
    elif re.findall(r'^show all', command.lower()):
        print(show_all_func(contacts))
    else:
        print(bad_command_func())

def hello_func():
    return 'Hi! How can I help you?'


def exit_func():
    return 'Good bye!'


def add_func(command, contacts):
    new_data = command.split(' ')
    if new_data[1] in contacts:
        raise IndexError
    elif re.findall(r'[^a-zA-Z]', new_data[1]) or re.findall(r'[^0-9-()]', new_data[2]):
        raise ValueError
    else:
        contacts[new_data[1]] = new_data[2]
        return f'{new_data[1]}:{contacts[new_data[1]]}'


def change_func(command, contacts):
    new_data = command.split(' ')
    print(new_data)
    if new_data[1] not in contacts:
        raise KeyError
    elif re.findall(r'[^0-9-()]', new_data[2]):
        raise ValueError
    else:
        contacts[new_data[1]] = new_data[2]
        return f'{new_data[1]}:{contacts[new_data[1]]}'


def phone_func(command, contacts):
    new_data = command.split(' ')
    print(contacts[new_data[1]])


def show_all_func(contacts):
    return contacts


def help_func():
    return '''Бот принимает команды:
                  -"hello", отвечает в консоль "How can I help you?"
                  -"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт обязательно через пробел.
                  -"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта обязательно через пробел.
                  -"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
                  -"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
                  -"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу'''


def bad_command_func():
    raise TypeError


contacts = {}


if __name__ == '__main__':
    main()

