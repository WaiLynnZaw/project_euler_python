# recursion depth exceeded
# def get_fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return get_fibonacci(n - 1) + get_fibonacci(n - 2)

def find_fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        x = str(a)
        if len(x) == 1000:
            print i
            break
        a, b, = b, a + b

find_fibonacci(100000)
