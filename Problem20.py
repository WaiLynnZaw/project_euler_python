def factorial(n):
  factorialValue = 1
  while n > 1:
    factorialValue *= n
    n -= 1
  return factorialValue

def sumOfFactorial(n):
    result = 0
    for i in str(factorial(n)):
        result += int(i)
    return result

print(sumOfFactorial(100))
