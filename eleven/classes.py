from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone:
    @Field.value.setter
    def value(self, value):
        if len(value) < 10 or len(value) > 12:
            raise ValueError("Phone must be 10 or 12 symbols.")
        if not value.isnumeric():
            raise ValueError("Phon can contains only numbers")
        self._value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        birthday_date = datetime.strptime(value, '%Y-%m-%d')
        if birthday_date > today:
            raise ValueError("Birthday must be less than current year and date.")
        self._value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def get_info(self):
        list_phones = ''
        for phone in self.phones:
            list_phones += f'phone.value'
        return f'{self.name.value} : {list_phones[:-1]}'

    def add_phones(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        for record in self.phones:
            if record == phone:
                self.phones.remove(record)
                return True
        return False

    def change_phones(self, phone):
        for record in phone:
            if not self.del_phone(record):
                self.add_phones(record)

    def add_birthday(self, date):
        self.birthday_date = Birthday(date)

    def days_to_birthday(self):
        if not self.birthday_date:
            raise ValueError("This contact doesn't have attribute birthday")
        today = datetime.now().date()
        birthday = datetime.strptime(self.birthday_date.value, "%Y-%m-%d").date()
        next_birthday_year = today.year
        if today.month > birthday.month and today.day > birthday.day:
            next_birthday_year += 1
        next_birthday = datetime(year=next_birthday_year, month=birthday.month, day=birthday.day)
        return (next_birthday - today).days


class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

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

    def iterator(self, count=5):
        page = []
        i = 0
        for record in self.data.values():
            page.append(record)
            i += 1
            if i == count:
                yield page
                page = []
                i = 0

