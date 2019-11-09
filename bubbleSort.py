def bubble_sort(num):
	swapped = True

	while swapped:
		swapped = False

		for i in range(len(num)-1):
			if (num[i] > num[i+1]):
				num[i], num[i+1] = num[i+1], num[i]
				swapped = True

numbers = input("Enter numbers with spaces: ")
numbers =numbers.split()
numbers = list(map(int,numbers))
bubble_sort(numbers)
print(numbers)