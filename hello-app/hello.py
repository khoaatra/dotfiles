#!/usr/bin/env python3
"""A small styled "hello" greeter."""

import argparse
import shutil
from datetime import datetime

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"


def time_of_day_greeting() -> str:
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    if hour < 18:
        return "Good afternoon"
    return "Good evening"


def build_box(message: str) -> str:
    width = min(shutil.get_terminal_size(fallback=(80, 24)).columns - 4, len(message) + 8)
    width = max(width, len(message) + 4)
    top = f"{CYAN}╭{'─' * width}╮{RESET}"
    bottom = f"{CYAN}╰{'─' * width}╯{RESET}"
    padded = message.center(width)
    middle = f"{CYAN}│{RESET}{BOLD}{MAGENTA}{padded}{RESET}{CYAN}│{RESET}"
    return "\n".join([top, middle, bottom])


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a styled greeting.")
    parser.add_argument("--name", default="world", help="who to greet")
    args = parser.parse_args()

    print(build_box(f"{time_of_day_greeting()}, {args.name}!"))


if __name__ == "__main__":
    main()
