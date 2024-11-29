def calculatePi(digits):
  result = 0
  return result

number_of_digits = input()
print(calculatePi(number_of_digits))



#its this one

n = int(input("enter iteration number: "))
pi = sum(4 * (-1) ** i / (2 * i + 1) for i in range(n))
print(f"Result using {n} : {pi}")