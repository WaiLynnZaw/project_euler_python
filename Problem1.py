def is_divisible(num):
    return num % 3 == 0 or num % 5 == 0

numbers = [i for i in range(1000) if is_divisible(i)]
print sum(numbers)
