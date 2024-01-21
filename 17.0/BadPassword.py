# number of iterated sequences
n = int(input())
sequences = []
for _ in range(n):
    _, *sequence = input().split()
    sequences.append(set(sequence))

# number of password changes
p = int(input())
password_changes = [input().split() for _ in range(p)]

def can_express(s1, s2):
    prefix, suffix = "", ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break

    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i] == s2[-i]:
            suffix = s1[-i] + suffix
        else:
            break

    if len(suffix) == 0:
        ps1 = s1[len(prefix) :]
        ps2 = s2[len(prefix) :]
    else:
        ps1 = s1[len(prefix) : -len(suffix)]
        ps2 = s2[len(prefix) : -len(suffix)]
    return ps1, ps2


for old_password, new_password in password_changes:
    if old_password == new_password:
        print("REJECT")
        continue
    ps1, ps2 = can_express(old_password, new_password)
    if ps1 == old_password:
        print("OK")
        continue

    for seq in sequences:
        count = 0

        for str in seq:
            if ps1 in str and str in old_password:
                count += 1
            if ps2 in str and str in new_password:
                count += 1

        if count == 2:
            print("REJECT")
            break

    else:
        print("OK")
