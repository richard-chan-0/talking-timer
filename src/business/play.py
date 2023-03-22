from datetime import datetime, timedelta
from time import sleep
import os


def play(message, interval, duration):
    start = datetime.now()
    end = start + timedelta(seconds=duration)
    os.system('say "starting session"')

    while start < end:
        sleep(interval)
        os.system(f'say "{message}"')
        start = datetime.now()

    os.system('say "session complete"')
