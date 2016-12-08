door_id = "abbhdwsy"

import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s.encode())
    return m.hexdigest()

password = ""
j = 0
while len(password) < 8:
    hash = md5(door_id + str(j))
    if hash.startswith("00000"):
        password += hash[5]
        print(password, j)
    j += 1

print(password)
