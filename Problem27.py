def is_prime_num(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def get_quadratic(n, a, b):
    return n ** 2 + a * n + b


def get_largest_product():
    prime_numbers = [i for i in xrange(2, 1000) if is_prime_num(i)]
    primes = prime_numbers[:]
    largest = 0
    for b in prime_numbers:
        for a in prime_numbers:
            i = 0
            while True:
                quadratic = get_quadratic(i, a, b)
                if quadratic not in primes:
                    if is_prime_num(quadratic):
                        primes.append(quadratic)
                    else:
                        if i - 1 > largest:
                            largest = i - 1
                            result = a * b
                        break
                i += 1
            i = 0
            # negative a and positive b
            while True:
                quadratic = get_quadratic(i, -a, b)
                if quadratic not in primes:
                    if is_prime_num(quadratic) and quadratic > 0:
                        primes.append(quadratic)
                    else:
                        if i - 1 > largest:
                            largest = i - 1
                            result = -1 * a * b
                        break
                i += 1

    print(result)


get_largest_product()
