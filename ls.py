from pathlib import Path
import re


def main(working_dir=".", pattern=".*"):
    p = Path(working_dir)
    if not p.exists():
        return
    for f in p.iterdir():
        if f.is_file() and re.match(pattern, f.name):
            try:
                print(f.absolute())
            except UnicodeEncodeError:
                pass


if __name__ == "__main__":
    import sys

    main(*sys.argv[1:])