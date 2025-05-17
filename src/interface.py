import subprocess
import sys


def clear_terminal():
    input('Enter any key to continue..')
    if sys.platform == 'win32':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def choice():
    key = input(f'''\
Enter:
1. To read your txt file
2. To make csv table (if you already read your txt`s)
q. exit
Your enter: ''')
    if key not in {'q', '1', '2'}:
        raise ValueError('ERROR: wrong key')
    return key

def ready_choice():
    while True:
        try:
            return choice()
        except ValueError as _ex:
            print(_ex)
            clear_terminal()

def enter_txt_name() -> str:
    name = input('Enter your name of your txt file would you like to read.\nType = file.txt: ')
    if '.txt' not in name:
        raise ValueError('ERROR: file must be with "*.txt" extension..')
    return name

def enter_with_ex() -> str:
    while True:
        try:
            return enter_txt_name()
        except ValueError as _ex:
            print(_ex)
            clear_terminal()

def read_txt(obj, name):
    while True:
        try:
            obj.get_ips(f'./txt/{name}')
            print(f'File {name} has been read success!')
            return
        except ValueError as _ex:
            print(_ex)
            clear_terminal()

def make_csv(maker):
    csv_name = input('Enter your name of your cvs file would you like to make.\nType = my_table: ')
    try:
        maker.list_processing()
        maker.write_csv(csv_name)
        print(f'{csv_name}.csv has been write successfully!')
    except:
        print('ERROR: something went`s wrong')
