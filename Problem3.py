def is_prime_num(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


prime_numbers = [i for i in xrange(2, 10000) if is_prime_num(i)]


def get_largest_prime(num):
    result = 0
    for i in prime_numbers:
        if num % i == 0:
            result = i
    return result


print(get_largest_prime(600851475143))
