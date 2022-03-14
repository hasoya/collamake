"""Create collage from images in a folder."""
from argparse import ArgumentParser
from pathlib import Path

from collamake.make import CollaMake

if __name__ == "__main__":
    parser = ArgumentParser(description="A simple collage maker")
    parser.add_argument("-f", "--file", type=Path, required=True)
    args = parser.parse_args()

    cm = CollaMake(args.file)
    cm.generate()
