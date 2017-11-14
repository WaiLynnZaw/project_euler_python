import time
 
start = time.time()


def find_fibonacci(n):
    fibonacci_num = []
    a, b = 0, 1
    for i in range(2, n):
        if a > 4000000:
            print(sum(fibonacci_num))
            break
        if is_even(a):
            fibonacci_num.append(a)
        a, b, = b, a + b
    return fibonacci_num


def is_even(num):
    return num % 2 == 0


print(find_fibonacci(10000))
print(time.time() - start)
