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

    # check for hypernet ABBA
    m = re.search(r'(.)((?!\1).)\2\1', " ".join(hypernet))
    if m:
        print("reject " + ip + str(m))
        return False

    # check for non-hypernet ABBA:
    m = re.search(r'(.)((?!\1).)\2\1', " ".join(other))
    if m:
        print("candidate: " + ip + str(m))
        return True

    return False

if __name__ == "__main__":
    count = 0
    for ip in open("7.input").readlines():
        if check_ip(ip):
            count += 1
    print(count)
