import argparse
import os
from pathlib import Path

import mido


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file", type=Path)
    parser.add_argument("-o", "--output_file", type=Path, default="output.txt")

    args = parser.parse_args()

    mid = mido.MidiFile(args.input_file)

    wait = 0
    events = []

    for msg in mid:
        wait += msg.time

        if msg.type != "note_on" or msg.velocity <= 10:
            continue

        events.append((msg.note - 69, wait))
        wait = 0

    with open(args.output_file, "w") as f:
        f.write("\n".join([f"{x[0]} {x[1]}" for x in events]))


if __name__ == "__main__":
    main()
