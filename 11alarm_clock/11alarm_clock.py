from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    count_down = 0
    print(CLEAR)
    while count_down <= seconds:

        time.sleep(1)   
        time_left = seconds - count_down
        count_down += 1
        minute_left = time_left // 60
        second_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minute_left:02d}:{second_left:02d}")

    playsound("alarm.mp3")

minute = int(input("How many minutes to wait: "))
second = int(input("How many seconds to wait: "))
total_seconds = minute * 60 + second

alarm(total_seconds)