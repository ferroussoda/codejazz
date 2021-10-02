# openssl enc -aes-256-cbc -salt

def solution(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1

    print(d, l, "L stores strlen")
    for p in range(1, l+1): # L stores strlen,  But why l+1?
        ok = True
        for i in range(l - p): # doubt on l-p, should be just l
            if d[l-i] != d[l-i - p]:
                print(l-i, l-i-p, d[l-i], d[l-i-p], "i=", i, p)
                ok = False
                break
        if ok:
            return p
    return -1


import rand
print(solution(rand()))
