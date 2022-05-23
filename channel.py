from pytube import Channel
from concurrent.futures.thread import ThreadPoolExecutor


def main(channel_url, limit):
    channel = Channel(channel_url)
    for (url, i) in zip(channel.video_urls, range(limit)):
        print(url)
    return


if __name__ == "__main__":
    import sys
    args = sys.argv
    main(sys.argv[1], int(sys.argv[2]))
