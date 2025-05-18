import os
import subprocess
import sys
import pathlib

def clear_terminal():
    if sys.platform == 'win32':
        subprocess.run('cls', shell=True)
    else:
        subprocess.run('clear', shell=True)

def continue_processing():
    input('Enter any key to continue..')
    clear_terminal()

def choice():
    key = input(f'''\
Enter:
1. To read your txt file
2. To make csv table (if you already read your txt`s)
3. To add ip`s to existing table (if you already read your txt`s)
4. To erase all txt files
q. exit
Your enter: ''')
    if key not in {'q', 'Q', '1', '2', '3', '4'}:
        raise ValueError('ERROR: wrong key')
    return key

def ready_choice():
    while True:
        try:
            return choice()
        except ValueError as _ex:
            print(_ex)
            continue_processing()

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
            continue_processing()

def read_txt(obj, name):
    while True:
        try:
            obj.get_ips(f'./txt/{name}')
            print(f'File {name} has been read success!')
            return
        except ValueError as _ex:
            print(_ex)
            continue_processing()

def make_csv(maker):
    csv_name = input('Enter your name of your cvs file would you like to make.\nType = my_table: ')
    try:
        maker.list_processing()
        maker.write_csv(csv_name)
        print(f'{csv_name}.csv has been write successfully!')
    except Exception as _ex:
        print('ERROR: something went`s wrong')
        print(f'Info: {_ex}')

def show_files(dir_name):
    try:
        my_dir = pathlib.Path(__file__).parent.parent / f'{dir_name}'
        if not my_dir.exists():
            raise Exception(f'Directory "{dir_name}" is not found..')
        csv_files = [file for file in os.listdir(my_dir) if str(file)[-4:] == '.csv']
        if len(csv_files) == 0:
            raise Exception(f'Directory "{dir_name}" doesn`t contain csv files..')
        print('Available files:')
        for index, file in enumerate(csv_files,1):
            print(f'{index}. {file.replace('.csv', '')}')
    except Exception as _ex:
        print(f'Error while receiving csv files')
        print(f'Info: {_ex}')

def choose_file(maker, dir_name):
    try:
        show_files(dir_name)
        dir_path = pathlib.Path(__file__).parent.parent / dir_name
        while True:
            user_input = input("\nEnter file number or name (without .csv): ").strip()
            csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
            if user_input.isdigit():
                index = int(user_input) - 1
                if 0 <= index < len(csv_files):
                    selected_file = csv_files[index].replace('.csv', '')
                    maker.list_processing()
                    maker.append_csv(selected_file)
                    print(f'New info was added to {selected_file} successfully!')
                    return
                raise Exception(f"Please enter number between 1 and {len(csv_files)}")
            raise Exception(f"Your input is not digit")
    except Exception as _ex:
        print(f"\nError while selecting file: {_ex}")
        print(f'Info: {_ex}')

def run_program(maker):
    key = ready_choice()
    try:
        if key == '1':
            file = enter_with_ex()
            read_txt(maker, file)
            continue_processing()
        elif key == '2':
            make_csv(maker)
            continue_processing()
        elif key == '3':
            clear_terminal()
            directory = 'csv'
            choose_file(maker, directory)
            continue_processing()
        elif key == '4':
            maker.clear_lists()
            print('All previous txt file entries have been erased')
            continue_processing()
        elif key in {'q', 'Q'}:
            exit(0)
    except ValueError as _ex:
        print(_ex)
