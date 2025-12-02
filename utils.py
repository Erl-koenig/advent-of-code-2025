from pathlib import Path


def load_input(day):
    filename = f"input/day{day:02}.txt"
    path = Path(filename)
    return path.read_text().strip()
