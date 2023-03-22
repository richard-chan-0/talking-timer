#!/usr/bin/env python3

from src.config.arg_parser import get_arguments
from src.business.play import play


def main():
    args = get_arguments()
    message = args.message
    duration = args.duration
    interval = args.interval

    play(message, interval, duration)


if __name__ == "__main__":
    main()
