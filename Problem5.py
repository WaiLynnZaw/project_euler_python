def gcd(n1, n2):
    if n1 == n2:
        return n1

    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    else:
        return n1


def lcm(n1, n2):
    return int(n1 * n2 / gcd(n1, n2))


def get_smallest_multiple():
    result = 1
    for i in xrange(2, 21):
        result = lcm(i, result)
    return result


print(get_smallest_multiple())
