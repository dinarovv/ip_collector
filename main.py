from src.interface import *
from src.list_maker import IPList


def main():
    maker = IPList()
    while True:
        key = ready_choice()
        try:
            if key == '1':
                file = enter_with_ex()
                read_txt(maker, file)
                clear_terminal()
            elif key == '2':
                make_csv(maker)
                clear_terminal()
            elif key == 'q':
                exit(0)
        except ValueError as _ex:
            print(_ex)

main()