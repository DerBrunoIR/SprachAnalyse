from concurrent.futures.process import ProcessPoolExecutor
import functools
import io


def scan_text(file: str):
    with open(file, "r") as f:
        text = f.read()
    words = text.split(" ")
    stats = {}
    for word in words:
        if word in stats:
            continue
        count = words.count(word)
        stats.update({word: count})
    return stats


def print_stats(d: dict):
    r = list(d.items())
    r.sort(key=lambda x: x[1])
    return ";".join([
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


def main(files):
    with ProcessPoolExecutor(8) as exe:
        futures = exe.map(scan_text, files, chunksize=12)
        exe.shutdown(wait=True)
        results = [f for f in futures]
        result = functools.reduce(merge_dict, results)
        print(print_stats(result))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = sys.stdin.read().split("\n")
        files = [f for f in files if len(f) > 0]
    if files:
        main(files)
    else:
        raise ValueError("got no files")
    # main([r"D:\Audio\Simplicissimus\Warum wir Funk verlassen haben.txt"])
