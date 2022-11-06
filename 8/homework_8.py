from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthday_names = []
    result = {}
    names = ''
    for val in users:
        dif = val['birthday'] - datetime.now()
        print(timedelta(dif.days))
        if dif.days <= timedelta(days=7).days:
            if int(datetime.weekday(val['birthday'])) in (0, 5, 6):
                birthday_names.append(f'{val["name"]}')
                names = ', '.join(birthday_names)
                result['Monday'] = names
            else:
                birthday_names.clear()
                birthday_names.append(f'{val["name"]}')
                names = ', '.join(birthday_names)
                result[val['birthday'].strftime('%A')] = names
    print(result)


birthdays = [{
    'name': 'Bill',
    'birthday': datetime(year=2022, month=11, day=12)
            },
            {
    'name': 'Jill',
    'birthday': datetime(year=2022, month=11, day=11)
            },
            {
    'name': 'Kim',
    'birthday': datetime(year=2022, month=11, day=7)
            },
            {
    'name': 'Jan',
    'birthday': datetime(year=2022, month=11, day=9)
            }]

get_birthdays_per_week(birthdays)