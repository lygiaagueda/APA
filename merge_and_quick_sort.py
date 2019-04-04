#Merge sort

def mergeSort(array):
	if len(array) > 1:
		m = len(array) // 2

		L = array[:m]
		R = array[m:]

		mergeSort(L)
		mergeSort(R)

		i = 0
		j = 0
		k = 0

		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				array[k] = L[i]
				i = i + 1
			else:
				array[k] = R[j]
				j = j + 1
			k = k + 1

		while j < len(R):
			array[k] = R[j]
			j = j + 1
			k = k + 1

		while i < len(L):
			array[k] = L[i]
			i = i + 1
			k = k + 1

#Quick sort

def partition(array, inicio, fim):
	pivo = array[fim]
	i = inicio -1   

	for j in range(inicio, fim):
		if array[j] <= pivo:
			i = i+1
			array[i], array[j] = array[j], array[i]

	array[i+1], array[fim] = array[fim], array[i+1]

	return i+1

def quickSort(array, inicio, fim):
	if(inicio < fim):
		indice = partition(array, inicio, fim)

		quickSort(array, inicio, indice - 1)
		quickSort(array, indice + 1, fim)



def main():
	array = [10,35, 45, 64, 73, 98, 100, 37, 98,61]
	array1 = [10,35, 45, 64, 73, 98, 100, 37, 98,61]

	print("Array a ser ordenado pelo merge: %s\n" % str(array))

	mergeSort(array)

	print("Array ordenado pelo merge: %s\n" % str(array))

	print("Array a ser ordenado pelo quick: %s\n" % str(array1))

	quickSort(array1, 0, len(array1)-1)

	print("Array ordenado pelo quick: %s\n" % str(array1))

if __name__ == '__main__':
	main()