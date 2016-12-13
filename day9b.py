import re
import argparse
import logging

logger = logging.getLogger(__name__)


def decompress(s):
    r = ""
    while s:
        m = re.match(r"(.*?)\((\d+)x(\d+)\)(.*)", s)
        if m:
            r += m.group(1)
            repeat_len = int(m.group(2))
            repeat_count = int(m.group(3))
            repeated = m.group(4)[:repeat_len]
            r += repeated * repeat_count
            s = m.group(4)[repeat_len:]
        else:
            r += s
            s = ""
    return r


def decompressed_length(s):
    logger.debug(s)
    l = 0
    while s:
        m = re.match(r"(.*?)\((\d+)x(\d+)\)(.*)", s)
        if m:
            l += len(m.group(1))
            repeat_len = int(m.group(2))
            repeat_count = int(m.group(3))
            repeated = m.group(4)[:repeat_len]
            l += decompressed_length(repeated) * repeat_count
            s = m.group(4)[repeat_len:]
        else:
            l += len(s)
            s = ""
    return l


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    for line in args.file.readlines():
        print(decompressed_length(line.replace(" ", "")))


if __name__ == "__main__":
    main()
