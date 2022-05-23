from concurrent.futures import Future

from pytube import Channel, YouTube
from concurrent.futures.thread import ThreadPoolExecutor
import pandas as pd
from time import sleep
from random import randint
from pathlib import Path


def download_audio(video_url, output_path):
    vid = YouTube(video_url)
    try:
        stream = vid.streams.get_audio_only()
    except KeyError:
        return ""
    out = Path(output_path) / stream.default_filename
    if not out.exists():
        stream.download(output_path)
    return out


def main(urls, out):
    with ThreadPoolExecutor() as exe:
        results = exe.map(download_audio, urls, [out for _ in urls])
        exe.shutdown(wait=True)
        for r in results:
            print(r)


if __name__ == "__main__":
    import sys

    urls = sys.stdin.read().split("\n")
    urls = [f for f in urls if len(f) > 0]
    main(urls, *sys.argv[1:])
