from src.interface import *
from src.list_maker import IPList


def main():
    maker = IPList()
    while True:
        key = ready_choice()
        try:
            if key == '1':
                file = enter_txt_name()
                read_txt(maker, file)
            elif key == '2':
                make_csv(maker)
                input('Enter any key to continue..')
                print('\n' * 50)
            elif key == 'q':
                exit(0)
        except ValueError as _ex:
            print(_ex)

main()