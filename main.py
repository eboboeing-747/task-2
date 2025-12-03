import sys
import signal
import os

cols: int = 0
lines: int = 0

def hide_cursor() -> None:
    print('\033[?25l', end='')

def show_cursor() -> None:
    print('\033[?25h', end='')

def update_size() -> None:
    global cols
    global lines

    size: os.terminal_size = os.get_terminal_size()
    cols = size.columns
    lines = size.lines

def handle_resize(sig, frame) -> None:
    update_size()
    draw()

def clear() -> None:
    os.system('clear')

def move(x: int, y: int) -> None:
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()

def draw_at(x: int, y: int, contents: str) -> None:
    move(x, y)
    print(f'\033[{y};{x}H{contents}', end='')

def draw() -> None:
    global cols
    global lines

    clear()
    draw_at(1, 1, '󰁛')
    draw_at(1, lines, '󰁂')
    draw_at(cols, 1, '󰁜')
    draw_at(cols, lines, '󰁃')
    move(0, 0)

def main() -> None:
    signal.signal(signal.SIGWINCH, handle_resize)
    hide_cursor()

    try:
        update_size()
        draw()
        input()
    except KeyboardInterrupt:
        clear()
        show_cursor()

    show_cursor()

if __name__ == '__main__':
    main()
