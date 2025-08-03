import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the 'Speed Typing Test!'")
    stdscr.addstr("\nPress the enter to begin!")
    stdscr.refresh()
    stdscr.getkey()

def display_screen(stdscr, text, user_text, WPM):
    stdscr.addstr(1, 0, text)
    stdscr.addstr(0, 0, f"WPM: {WPM}")

    for i, char in enumerate(user_text):
        current_char = text[i]
        color = curses.color_pair(1)
        if char != current_char:
            color = curses.color_pair(2)
        stdscr.addstr(2, i, char, color)

def load_text():
    with open("text_file.txt","r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def WPM_test(stdscr):
    text = load_text()
    user_text = []
    WPM = 0
    stdscr.nodelay(True)
    start_time = time.time()

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        WPM = round(len(user_text) / (time_elapsed / 60) / 5)

        stdscr.clear()
        display_screen(stdscr, text, user_text, WPM)
        stdscr.refresh()

        if "".join(user_text) == text:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(user_text) > 0:
                user_text.pop()
        elif len(user_text) < len(text):
            user_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    start_screen(stdscr)
    while True:
        WPM_test(stdscr)
        stdscr.addstr(4, 0, "You completed the text! Type any key to continue...")
        
        key = stdscr.getkey()
        if ord(key) == 27:
            break

wrapper(main)


