def get_name():
    return input('Введите имя')

def get_last_name():
    return input('Введите фамилию')

def get_phone():
    while True:
        phone = input('Введите телефон: ')
        if phone.isdigit():
            return phone
        print('Некорректный телефон')

def get_comment():
    return input('Введите комментарий')

def choose_format():
    while True:
        format = input('Введите формат (столбец, строчка): ')
        if format in ('столбец', 'строчка'):
            return format
        print('Некорректный формат')

def export_console(data: tuple):
    print(f'Имя: {data[0]}\nФамилия: {data[1]}\nТелефон: {data[2]}\nКомментарий: {data[3]}')

def export_console_2(data: dict):
    for index, value in data.items():
        print(f'{index}: {value}')
