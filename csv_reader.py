#from csv_generator import data
from user_interface import export_console
data = 'file.csv'

def read_csv():
    with open(data, 'r') as rd:
        # rd.readlines()
        for i in rd:
            export_console(i.split(';'))
            #print(i)
        
#read_csv(data)
