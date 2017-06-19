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


def amicable_pairs(low, high):
    numbers = []
    pairs = []

    for i in range(low, high+1):
        numbers.append(sum_of_divisors(i))

    for i in range(high - low + 1):
        ind = numbers[i]
        if i + low < ind and low <= ind <= high and numbers[ind - low] == i + low:
            pairs.append([i + low, ind])
    return pairs


def sum_of_amicable_pairs(pairs):
    result = 0
    for pair in pairs:
        result += sum(pair)
    return result

print(sum_of_amicable_pairs(amicable_pairs(1, 100000)))
