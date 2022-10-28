import random
import cluster as cl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


#Clase Kmeans
class Kmeans:

    #Lista del numero de cluster
    clusters = []
    
    def __init__(self,data,k):
        self.data = data
        self.nombreColumnas = get_unique_values(data.iloc[:,-1].values.tolist())
        self.k = k
        self.filas = len(data)
        self.columnas = len(data.columns)

    def algoritmo(self):
        #Valores random de indices.
        random_indexes = random.sample(range(self.filas), self.k)
        #genero centroides randoms
        centroides = [self.data.iloc[i,:-1].values.tolist() for i in random_indexes]
        #Boleano para saber si tiene centroides diferentes
        centroidesDiferentes = True

        self.asignarCentroideaCluster(centroides)
        self.asignarIndividosaClusters(centroides)
        
        while centroidesDiferentes:
            nuevosCentroides = self.actualizarCentroides()

            if((len(nuevosCentroides) == len(centroides)) and (all(iterador in centroides for iterador in nuevosCentroides))):
                centroides = nuevosCentroides
                #Actualizo mi lista de clusters
                self.clusters.clear()
                self.asignarCentroideaCluster(centroides)
                self.asignarIndividosaClusters(centroides)
            else:
                centroidesDiferentes = False
        return self.clusters
    
    #ActualizarCentroides
    def actualizarCentroides(self):
        #Lista de nuevos centroides
        nuevosCentroides = []

        for iterador in range(self.k):
            nuevoCentroide = []
            individuos = self.clusters[iterador].individuos
            tamanio = len(individuos)
            for iterador2 in individuos:
                if len(nuevoCentroide)==0:
                    nuevoCentroide = iterador2[:-1].copy()
                else:
                    temporal = [iterador2[x] + nuevoCentroide[x] for x in range(len(nuevoCentroide))]
                    nuevoCentroide = temporal.copy()

            centroideTemporal = [x / tamanio for x in nuevoCentroide]
            nuevosCentroides.append(centroideTemporal)
        return nuevosCentroides
    
    def asignarIndividosaClusters(self,centroides):
        for iterador in range(self.filas):
            row = self.data.iloc[iterador,:].values.tolist()
            #Calculando la distancia(error)
            distancias = [calculardistancia(row[:-1],centroides[iterador2]) for iterador2 in range(self.k)]
            #Accedo al minimo de dicha dstancia
            minimoValor = min(distancias)
            #Accedo al indice del valor de la minima distancia
            indiceMinimoValor = distancias.index(minimoValor)
            #Añado la fila a mi lista de clusters
            self.clusters[indiceMinimoValor].anadirIndividuo(row)
    
    #Asignacion de centroides a cada cluster.
    def asignarCentroideaCluster(self,centroides):
        for iterador in centroides:
            nuevoCluster = cl.Cluster(iterador)
            #Añado el nuevo cluster a mi lista clusters.
            self.clusters.append(nuevoCluster)
    
    #Imprimir clusters
    def imprimirClusters(self):
        for iterador in range(self.k):
            print("Cluster",iterador,":")
            self.clusters[iterador].imprimirClusters()
    
    def graficarClusters(self,nombre):
        temporal = np.zeros((self.k, len(self.nombreColumnas)))
        dfs = pd.DataFrame(temporal,columns=self.nombreColumnas)
        for iterador in range(self.k):
            counter = self.clusters[iterador].get_frequency()
            for tissue in counter:
                dfs.at[iterador,tissue] = counter[tissue]
        dfs.plot.bar(rot=0)


def calculardistancia(centroide,filaActual):
    distancia = 0
    for iterador in range(len(centroide)):
        distancia += pow(centroide[iterador] - filaActual[iterador], 2)
    return math.sqrt(distancia)


def make_pairs(x_features):
    x_list = x_features.values.tolist()
    pairs = []
    for i in range(len(x_list)):
        new_object = cl.Pair(x_list[i], i)
        pairs.append(new_object)
    return pairs


def get_unique_values(values):
    list_of_unique_numbers = []
    unique_values = set(values)
    for value in unique_values:
        list_of_unique_numbers.append(value)
    return list_of_unique_numbers