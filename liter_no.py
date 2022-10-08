# openssl enc -aes-256-cbc -salt

def solution_fn(n):
    d = [0] * 30
    l = 0
    while (n > 0):
        d[l] = n % 2
        n //= 2
        l += 1

    print(d, l, "what is d and l in this statement?")
    for p in range(1, 1 + l): # L stores strlen,  ut why l+1?
        ok = True
        for i in range(l - p): # doubt on l-p, should be just l
            if d[l-i] != d[l-i - p]:
                print(l-i, l-i-p, d[l-i], d[l-i-p], "i=", i, p)
                ok = False
                break
        if ok:
            return p
    return -1


in = input('Enter a number')
print(solution_fn(int(in)))
