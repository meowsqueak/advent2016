import re

def check_ip(ip):
    hypernet = []
    other = []
    post = ip
    while post:
        pre, _, post = post.partition("[")
        if pre:
            other.append(pre)
        pre, _, post = post.partition("]")
        hypernet.append(pre)

    # find all ABAs
    aba = re.findall(r"(?=(.)(.)\1)", "  ".join(other))
    bab = re.findall(r"(?=(.)(.)\1)", "  ".join(hypernet))

    for x in aba:
        if x[0] != x[1]:
            if (x[1], x[0]) in bab:
                return True
    return False

if __name__ == "__main__":
    count = 0
    for ip in open("7.input").readlines():
        if check_ip(ip):
            count += 1
    print(count)
