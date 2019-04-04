import sys

class Grafo():
	def __init__(self, vertices):
		self.quantVertices = vertices
		self.matriz = []

	def min(self, chave, conjuntoDeVertices):
		minimo = float('inf')
	
		for i in range(self.quantVertices):
			if chave[i] < minimo and conjuntoDeVertices[i] == False:
				minimo = chave[i]
				indiceDoMinimo = i

		return indiceDoMinimo

	def Solucao(self, pais):
		custoTotal = 0

		for i in range(1, self.quantVertices):
			print(pais[i], '>>', i, ' ', 'com custo', self.matriz[i][pais[i]])
			custoTotal += self.matriz[i][pais[i]]

		print('Custo total:', custoTotal)

	def Prim(self):
		chaves = [float('inf')] * self.quantVertices
		pais = [None] * self.quantVertices
		pais[0] = -1
		chaves[0] = 0

		conjuntoDeVertices = [False] * self.quantVertices

		for i in range(self.quantVertices):
			u = self.min(chaves, conjuntoDeVertices)
			
			conjuntoDeVertices[u] = True

			for j in  range(self.quantVertices):
				if(self.matriz[u][j] > 0 and conjuntoDeVertices[j] == False and self.matriz[u][j] < chaves[j]):
					chaves[j] = self.matriz[u][j]
					pais[j] = u

		self.Solucao(pais)