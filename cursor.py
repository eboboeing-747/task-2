import sys

class Cursor:
    x: int = 0
    y: int = 0

    @staticmethod
    def move(x: int, y: int) -> None:
        sys.stdout.write(f'\033[{y};{x}H')
        sys.stdout.flush()

    @staticmethod
    def hide() -> None:
        print('\033[?25l', end='')

    @staticmethod
    def show() -> None:
        print('\033[?25h', end='')

cursor: Cursor = Cursor()
