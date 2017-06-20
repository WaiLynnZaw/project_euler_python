import time


start = time.time()


def reverse_number(n):
    return int(str(n)[::-1])


def is_palindrome(num):
    return num == reverse_number(num)


def get_largest_palindrome():
    result = 0
    for i in xrange(999, 100, -1):
        for j in xrange(i, 100, -1):
            product = i * j
            if product > result and is_palindrome(product):
                result = product

    print result

get_largest_palindrome()
print(time.time()-start)
