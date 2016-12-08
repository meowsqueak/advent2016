door_id = "abbhdwsy"

import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

password = ["_"] * 8
j = 0
count = 0
while count < 8:
    hash = md5(door_id + str(j))
    if hash.startswith("00000"):
        pos = int(hash[5], 16)
        if pos < 8 and password[pos] == "_":
            password[pos] = hash[6]
            print("".join(password) + "\r", end="")
            count += 1
    j += 1

print("".join(password))
