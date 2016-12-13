import re
import argparse


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()

    for line in args.file.readlines():
        result = decompress(line)
        print(len(result.replace(" ", "")))


if __name__ == "__main__":
    main()
