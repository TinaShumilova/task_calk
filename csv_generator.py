import user_interface as ui
#
def create():
    path = 'file.csv'
    in_colons = ui.choose_format() == 'столбец'
    name = ui.get_name()
    fam = ui.get_last_name()
    tel = ui.get_phone()
    comm = ui.get_comment()
    with open(path, 'a', encoding='1251') as data:
        if in_colons:
            data.write('\n')
            data.write(f'{name}\n')
            data.write(f'{fam}\n')
            data.write(f'{tel}\n')
            data.write(f'{comm}\n')
        else:
            data.write(f'{name};{fam};{tel};{comm}\n')
    return path
#
#create() # костыль для самопроверки
#
# комментарии аффтора: В функцию open() добавил аргумент encoding='1251',
# это кодовая страница "Windows кириллица". Исправилась проблема отображения
# в Экселе, Блокноте, но таки не в VSC. Здесь видимо решается по другому.
# Еще, по хорошему бы, название и путь к файлу передавать генератору
# аргументом, чтобы это задавалось на "верхнем" уровне, и генератор тут
# ничего бы не изобретал. Но править это уже похоже не будем, пора решать
# след задачи. 