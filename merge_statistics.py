import functools


def print_stats(d: dict):
    r = list(d.items())
    r.sort(key=lambda x: f"{x[1]}{x[0]}")
    return "\n".join([
        f"{k},{v}" for (k, v) in r
    ])


def merge_dict(x: dict, y: dict):
    x = x.copy()
    for (k, v) in y.items():
        if k in x:
            x[k] += v
        else:
            x[k] = v
    return x


def read_file(file):
    with open(file, "r") as f:
        text = f.read().split("\n")
    d = {}
    for line in text:
        if len(line) > 0:
            word, count = line.split(",")
            count = int(count)
            d[word] = count
    return d


def main(files):
    ds = [read_file(f) for f in files]
    d = functools.reduce(merge_dict, ds)
    print_stats(d)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = sys.stdin.read().split("\n")
        files = [f for f in files if len(f) > 0]
    main(files)
    # main([r"D:\Audio\Simplicissimus\Warum wir Funk verlassen haben.txt"])
