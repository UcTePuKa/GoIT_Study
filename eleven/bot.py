from classes import Record
from decorator import input_error

contacts = {}


@input_error
def hello_func():
    return 'Hi! How can I help you?'


@input_error
def exit_func():
    return 'Good bye!'


@input_error
def add_func(data):
    name, *phones = create_data(data)
    if name in contacts:
        raise ValueError('This contact already exist.')
    record = Record(name)
    for phone in phones:
        record.add_phones(phone)
    record.add_record(record)
    return f'You added new contact: {name} with this phone {phone}.'


@input_error
def change_func(data):
    name, phones = create_data(data)
    record = contacts[name]
    record.change_phones(phones)
    return 'Contacts were changed'


@input_error
def phone_search_func(value):
    return contacts.get(value.strip().get_info())


@input_error
def show_all_func():
    contacts = ''
    page_number = 1
    for page in contacts.iterator():
        contacts += f'Page number №{page_number}\n'
        for record in page:
            contacts += f'{record.get_info()}\n'
        page_number += 1
    return contacts

@input_error
def del_func(name):
    name = name.strip()
    contacts.remove_record(name)
    return "You deleted the contact."

@input_error
def del_phone_func(data):
    name, phone = data.strip().split(' ')
    record = contacts[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


@input_error
def birthday_func(data):
    name, date = data.strip().split(' ')
    record = contacts[name]
    record.add_birthday(date)
    return f'For {name} you add Birthday {date}'


@input_error
def next_birthday_func(name):
    name = name.strip()
    record = contacts[name]
    return f"Days to next birthday of this {name} will be in {record.get_days_to_next_birthday()}."


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
    name, *phones = data.strip().split(' ')
    if name.isnumeric():
        raise ValueError('Wrong name.')
    return name, phones


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

