#!/usr/bin/env python3
import os
import subprocess
from concurrent.futures.process import ProcessPoolExecutor
from pathlib import Path
import re

from vosk import Model, KaldiRecognizer, SetLogLevel

SetLogLevel(-1)
model = Model("vosk-model-small-de-0.15")
# model = Model("model-large")
sample_rate = 16000


def recognize(file):
    p = Path(file)
    if not p.exists():
        return "\r"
    else:
        rec = KaldiRecognizer(model, sample_rate)
        process = subprocess.Popen(['ffmpeg', '-loglevel', 'quiet', '-i', file, '-ar', str(sample_rate), '-ac', '1',
                                    '-f', 's16le', '-'], stdout=subprocess.PIPE)
        while True:
            data = process.stdout.read(8000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)
        result = rec.FinalResult().replace("\n", "")
        result = re.match('\{  \"text\" \: \"(?P<text>.+)\"\}', result).group("text")

    o = p.parents[0] / (p.stem + ".txt")
    o.write_text(result)
    return str(o.absolute())


def main(files):
    with ProcessPoolExecutor(12) as exe:
        results = exe.map(recognize, files, chunksize=12)
        exe.shutdown(wait=True)
    for path in results:
        print(path)


if __name__ == "__main__":
    import sys

    files = sys.stdin.read().split("\n")
    files = [f for f in files if len(f) > 0]
    if files:
        main(files)
    else:
        raise ValueError("got no filenames via stdin")
    # main([r"D:\Audio\Simplicissimus\Warum wir Funk verlassen haben.txt"])
