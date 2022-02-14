import csv_generator as gen
import csv_reader as red
import user_interface as ui

def write_file():
    # name = ui.get_name()
    # last_name = ui.get_last_name()
    # phone = ui.get_phone()
    # coment = ui.get_comment()
    gen.create()

def read_file():
    red.read_csv()
    #ui.export_console()