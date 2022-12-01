contacts = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command or parametrs, please try again.'
    return inner


@input_error
def hello_func():
    return 'Hi! How can I help you?'


@input_error
def exit_func():
    return 'Good bye!'


@input_error
def add_func(data):
    name, phone = create_data(data)
    if name in contacts:
        raise ValueError('This contact already exist.')
    contacts[name] = phone
    return f'You added new contact: {name} with this phone {phone}.'


@input_error
def change_func(data):
    name, phone = create_data(data)
    if name in contacts:
        contacts[name] = phone
        return f'You changed number to {phone} for {name}.'
    return 'This contact does not exist. Use add command plz.'


@input_error
def phone_search_func(name):
    if name.strip() not in contacts:
        raise ValueError('This contact does not exist.')
    return contacts.get(name.strip())


@input_error
def show_all_func():
    all_contacts = ''
    for key, value in contacts.items():
        all_contacts += f'{key} : {value} \n'
    return all_contacts

def help_func():
    return '''Бот принимает команды:
                  -"hello", отвечает в консоль "How can I help you?"
                  -"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт обязательно через пробел.
                  -"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта обязательно через пробел.
                  -"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
                  -"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
                  -"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу'''


commands = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    '.': exit_func,
    'add': add_func,
    'change': change_func,
    'show all': show_all_func,
    'phone': phone_search_func,
    'help': help_func
}


def change_input(user_input):
    new_input = user_input
    data = ''
    for key in commands:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input):]
            break
    if data:
        return reaction_func(new_input)(data)
    return reaction_func(new_input)()


def reaction_func(reaction):
    return commands.get(reaction, break_func)


def create_data(data):
    new_data = data.strip().split(" ")
    name = new_data[0]
    phone = new_data[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone


def break_func():
    return 'Wrong input.'


def main():
    while True:
        user_input = input('Enter command for bot: ')
        result = change_input(user_input)
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()

