import collections

#Clase Cluster
class Cluster:
    def __init__(self,centroide):
        self.centroid = centroide
        self.individuos = []
    
    #Añado un nuevo individuo a mi lista de individuos
    def anadirIndividuo(self,individuo):
        self.individuos.append(individuo)
    
    #Imprime mi lista de individuos
    def imprimirIndividuos(self):
        tamanio = len(self.individuos[0])
        for iterador in self.individuos:
            print(iterador[tamanio-1])
    
    #Contador
    def get_frequency(self):
        tamanio = len(self.individuos[0])
        tissues = []
        for iterador in self.individuos:
            tissues.append(iterador[tamanio-1])
        counter = collections.Counter(tissues)
        return counter


#Clase Pareja
class Pareja:
    def __init__(self, individuo, id):
        #asignar cluster inicial de -1
        self.cluster = -1
        self.data = individuo
        self.id = id

    #Asignacion del nuevo cluster
    def asignarCluster(self, nuevoCluster):
        self.cluster = nuevoCluster

    #Funcion para imprimir
    def imprimirPareja(self,lista):
        print("{",self.cluster,",",lista[self.id],"}")

    #funcion comparacion
    def __eq__(self, other):
        comparison = self.data == other.data
        equal_arrays = comparison.all()
        return equal_arrays