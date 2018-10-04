def listToString(a):
    return str(a)


def addBorder(a):
    res = []
    side = '+' + '-' * len(a[0]) + '+'
    res.append(side)
    for s in a:
        res.append('|' + s + '|')
    res.append(side)
    return res


def shorting(e):
    res = []
    for s in e:
        if len(s) <= 10:
            res.append(s)
        else:
            res.append(s[0] + str(len(s) - 2) + s[len(s) - 1])
    return res


def competition(e, k):
    while (k < len(e) - 1 and e[k] > 0 and e[k] == e[k + 1]):
        k += 1
    while (k >= 0 and e[k] == 0):
        k -= 1
    return k + 1


def goodPairs(a, b):
    return sorted(list({i * i + j * j for i in a for j in b
                        if i * j % (i + j) == 0}))


def makeShell(n):
    s = [0] * n
    res = []
    for i in range(2 * n - 1):
        res.append(s[:n - abs(n - 1 - i)])
    return res
