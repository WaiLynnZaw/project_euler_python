import time
#Optimized the execution time with prime


start_time = time.time()


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


prime_numbers = [i for i in xrange(2, 1000) if is_prime(i)]


def recurring_cycle(d):
    for t in range(1, d):
        if 1 == 10 ** t % d:
            return t
    return 0


longest = max(recurring_cycle(i) for i in prime_numbers)
print([i for i in prime_numbers if recurring_cycle(i) == longest][0], "%s seconds" % str(time.time() - start_time))
