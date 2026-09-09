import argparse
from pathlib import Path

def parse_args(): # If you wish to change any default setting, change the value in here
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    return parser.parse_args()