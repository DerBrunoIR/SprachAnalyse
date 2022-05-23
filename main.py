from subprocess import Popen, PIPE
from vosk import Model, KaldiRecognizer, SetLogLevel
from pytube import Channel, YouTube


def main(url, n, out):
    get_urls = Popen(["python", "channel.py", url, str(n)], stdout=PIPE)
    download_vids = Popen(["python", "getAudio.py", out], stdin=get_urls.stdout, stdout=PIPE)
    convert_to_text = Popen(["python", "speech2text.py"], stdin=download_vids.stdin)
    stats = Popen(["python", "statistics.py"], stdin=convert_to_text.stdout)
    out, err = stats.communicate()
    print(out)


if __name__ == "__main__":
    import sys

    channel_url, count, output = sys.argv[1:]
    main(channel_url, count, output)
