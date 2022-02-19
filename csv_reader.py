from user_interface import export_console, export_console_2

data = 'file.csv'

def read_csv(version = 1): # Не знаю как бyдет организация выбора строчек и столбцов
    if version == 1:    
        with open(data, 'r') as dt:
            for item in dt:
                export_console(item.split(';'))  # строка, но для этого в ui в этом методе надо поменять вывод
    else: 
        with open(data, 'r') as dt: # столбец
            for item in dt:
                line_dt = item.split(';')
                dic = {
                    'Имя': line_dt[0],
                    'Фамилия': line_dt[1],
                    'Телефон' : line_dt[2],
                    'Коментарий': line_dt[3]}
                export_console_2(dic)
        