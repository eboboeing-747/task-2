import signal
import os
from cursor import cursor as cursor

def clear() -> None:
    os.system('clear')

def update_size() -> None:
    size: os.terminal_size = os.get_terminal_size()
    cursor.x = size.columns
    cursor.y = size.lines

def handle_resize(sig, frame) -> None:
    update_size()
    draw()

def draw_at(x: int, y: int, contents: str) -> None:
    cursor.move(x, y)
    print(f'\033[{y};{x}H{contents}', end='')

def draw() -> None:
    clear()
    draw_at(1, 1, '󰁛')
    draw_at(1, cursor.y, '󰁂')
    draw_at(cursor.x, 1, '󰁜')
    draw_at(cursor.x, cursor.y, '󰁃')

    resolution: str = f'{cursor.x}x{cursor.y}'
    res_col: int = (cursor.x - len(resolution)) // 2 + 1
    res_line: int = cursor.y // 2 if cursor.y % 2 == 0 else cursor.y // 2 + 1

    if len(resolution) < cursor.x - 2 or cursor.y >= 3:
        draw_at(res_col, res_line, resolution)

    cursor.move(0, 0)

def main() -> None:
    signal.signal(signal.SIGWINCH, handle_resize)
    cursor.hide()

    update_size()
    draw()

    try:
        input()
    except KeyboardInterrupt:
        pass

    clear()
    cursor.show();

if __name__ == '__main__':
    main()

