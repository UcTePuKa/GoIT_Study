from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name:
    pass


class Phone:
    pass


class AdressBook(UserDict):
    def __init__(self, record):
        self.data[record.name.vaulue] = record

    def get_all(self):
        return self.data

    def has_record(self, name):
        if self.data.get(name):
            return True
        else:
            return False

    def get_record(self, name):
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.has_record(value)
        for record in self.get_all().values():
            for phone in record.phones:
                if phone.value == value:
                    return record
        raise ValueError("Contact with this value does not exist.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def get_info(self):
        phones_for_list = ''
        for phone in self.phones:
            phones_for_list += f'{phone.value}, '
        return f'{self.name.value} : {phones_for_list[:-1]}'

    def add_phones(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        for record in self.phones:
            if record == phone:
                self.phones.remove(record)
                return 1
        return 0

    def phones_change(self, phone):
        for phones in phone:
            if not self.del_phone(phones):
                self.add_phones(phones)






