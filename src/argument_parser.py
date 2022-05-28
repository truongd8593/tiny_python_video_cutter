import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument(
        "file_name",
        type=str,
        help="Path to video file"
    )
    parser.add_argument(
        "start_time",
        type=int,
        help="Start time in minutes"
    )
    parser.add_argument(
        "end_time",
        type=int,
        help="End time in minutes"
    )
    parser.add_argument(
        "--target_name",
        type=int,
        help="Target file name"
    )
    arguments = parser.parse_args()
    return arguments