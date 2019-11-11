def insertionSort(l):
	for i in range(1, len(l)):
		item_to_insert = l[i]
		j = i - 1
		while j >= 0 and l[j] > item_to_insert:
			l[j + 1] =l[j]
			j -= 1
			l[j + 1] = item_to_insert
	return l

numbers = input("Enter multiple number with space: ")
numbers = numbers.split()
numbers = list(map(int, numbers))
s = insertionSort(numbers)
print(s)
