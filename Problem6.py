sum_of_squares = sum([i**2 for i in range(1, 101)])
square_of_sums = sum([i for i in range(1,101)]) ** 2

print (square_of_sums - sum_of_squares)
