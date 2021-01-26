#fibonacci numbera
def fibonacci(i):
	numbers = []
	x, y = 0, 1
	h = i - 2
	numbers.append(x)
	numbers.append(y)
	for j in range(1, h):
		fib = numbers[j] + numbers[j-1]
		numbers.append(fib)
	print(numbers)

#test
print(fibonacci(20))