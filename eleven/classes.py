from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def val(self, value):
        self._value = value


class Name:
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if len(value) < 10 or len(value):
            raise ValueError('Phone must have from 10 to 12 numbers')
        if not value.isnumeric():
            raise ValueError('Phone contains only numbers')
        self._value = value

class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        birth_date = datetime.strptime(value, '%Y-%m-%d')
        if birth_date > today:
            raise ValueError('Birthday must be before today')



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

    def iterator(self, count = 5):
        page = []
        i = 0
        for record in self.data.values():
            page.append(record)
            i += 1
            if i == count:
                yield page
                page = []
                i = 0
        if page:
            yield page


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.phones = []
        self.birth_date = None

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

    def get_birthday(self, date):
        self.birth_date = Birthday(date)

    def days_to_birthday(self):
        if not self.birth_date:
            raise ValueError("This contact doesn't have attribute birthday")
        today = datetime.now().date()
        birth_date = datetime.strptime(self.birth_date, '%Y-%m-%d').date()
        next_year = today.year
        if today.month >= birth_date.month and today.day >= birth_date.month:
            next_year += 1
        next_birthday = datetime(year=next_year, month=birth_date.month, day=birth_date.day)
        return (next_birthday.date() - today).days






