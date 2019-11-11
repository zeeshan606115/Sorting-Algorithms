def selectionSort(l):
	for i in range(len(l)):
		min_value_index = i

		for j in range(i+1, len(l)):
			if l[j] < l[min_value_index]:
				min_value_index = j


		l[i], l[min_value_index] = l[min_value_index], l[i]
	return l

numbers = input("Enter multiple number with space: ")
numbers = numbers.split()
numbers = list(map(int, numbers))
s = selectionSort(numbers)
print(s)
