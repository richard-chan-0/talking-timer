import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        prog="Interval Beeper",
        description="utility to have computer say a message during set interval",
    )

    parser.add_argument(
        "-d", "--duration", help="duration of session", type=int, default=60
    )
    parser.add_argument(
        "-m",
        "--message",
        help="message for utiity",
        type=str,
        default="interval complete",
    )
    parser.add_argument(
        "-i", "--interval", help="interval for lap", type=int, default=30
    )

    return parser.parse_args()
