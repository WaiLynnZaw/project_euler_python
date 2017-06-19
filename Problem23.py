import math


def divisor_generator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def sum_of_divisors(n):
    result = 0
    for i in list(divisor_generator(n)):
        if i != n:
            result += i
    return result


def is_abundant(num):
    if num < sum_of_divisors(num):
        return True
    else:
        return False


ab = [i for i in xrange(12, 28123) if is_abundant(i)]
not_ab_sum = [i for i in xrange(28123)]

for i in xrange(len(ab)):
    for j in xrange(i, 28123):
        if ab[i] + ab[j] < 28123:
            not_ab_sum[ab[i] + ab[j]] = 0
        else:
            break
print sum(not_ab_sum)
