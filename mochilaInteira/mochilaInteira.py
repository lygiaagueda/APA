import numpy as np

def mochilaInteira(W, p, v, n):
	memo = np.zeros((n+1, W+1))

	for i in range(0, n+1):
		for m in range(0, W+1):
			if i == 0 or m == 0:
				memo[i][m] = 0
			elif p[i-1] <= m:
				memo[i][m] = max(v[i-1] + memo[i-1][m - p[i-1]], memo[i-1][m])
			else:
				memo[i][m] = memo[i-1][m]

	return memo[n][W]

def main():
	peso = []
	valor = []
	n = 0
	W = 0
	count = 0

	for line in open('mochila01.txt.txt'):
		line = line.rstrip('\n')
		if count == 0:
			x = (line.split(' '))
			n = int(x[0])
			W = int(x[1])

			count = 1
			continue

		aux = (line.split(' '))

		peso.append(int(aux[0]))
		valor.append(int(aux[1]))

	print("Lista de itens no formato \"peso valor\":")
	for i in range(0, len(peso)):
		print(peso[i], valor[i])
	
	print("\nSolucao:")
	print(mochilaInteira(W, peso, valor, n))


if __name__ == '__main__':
	main()