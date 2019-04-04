import sys

class Grafo():
	def __init__(self, vertices):
		self.quantVertices = vertices
		self.matriz = []

	def DistanciaMinima(self, distancias, conjuntoDeVertices):
		minimo = float('inf')
	
		for i in range(self.quantVertices):
			if distancias[i] < minimo and conjuntoDeVertices[i] == False:
				minimo = distancias[i]
				indiceDoMinimo = i

		return indiceDoMinimo

	def Solucao(self, distancias):
		custoTotal = 0

		for i in range(1, self.quantVertices):
			print(i, ' ---- ', distancias[i])
			custoTotal += distancias[i]

		print('Custo total:', custoTotal)

	def Dijkstra(self):
		distancias = [float('inf')] * self.quantVertices
		distancias[0] = 0

		conjuntoDeVertices = [False] * self.quantVertices

		for i in range(self.quantVertices):
			u = self.DistanciaMinima(distancias, conjuntoDeVertices)
			
			conjuntoDeVertices[u] = True

			for j in  range(self.quantVertices):
				if(self.matriz[u][j] > 0 and conjuntoDeVertices[j] == False and distancias[j] > distancias[u] + self.matriz[u][j]):
					distancias[j] = distancias[u] + self.matriz[u][j]

		self.Solucao(distancias)