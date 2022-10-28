import leerdataset as dataset
import kmeans as km


datasetCompleta, x_features = dataset.parse_data()


def kmeans(cantidadPruebas):

    kmeans = km.Kmeans(datasetCompleta,4)
    kmeans.algoritmo()

kmeans(4)
