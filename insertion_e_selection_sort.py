def InsertionSort(array):
	for i in range(1, len(array)):
		pivo = array[i]

		j = i - 1

		while j >= 0:
			if pivo < array[j]:
				array[j+1], array[j] = array[j], array[j+1]
				j -= 1
			else:
				break

		array[j+1] = pivo

	return array

def SelectionSort(array):
	for i in range(0, len(array)):
		minimo = i

		for j in range(i+1, len(array)):
			if array[minimo] > array[j]:
				minimo = j

		array[i], array[minimo] = array[minimo], array[i]

	return array


def main():
	array = [9, 21, 32, 64, 21, 40, 73, 10, 5, 2]
	array1 = [9, 21, 32, 64, 21, 40, 73, 10, 5, 2]

	"""
	# Melhor caso:
	array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	"""
	"""
	# Pior caso:
	array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	array1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
	"""

	print("Array original: %s\n" % str(array))

	print("Array ordenado com Insertion Sort: %s\n" % InsertionSort(array))

	print("Array ordenado com Selection Sort: %s\n" % SelectionSort(array1))


if __name__ == '__main__':
	main()
