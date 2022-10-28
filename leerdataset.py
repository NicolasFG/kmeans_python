import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



#Analisis de la data.
def parse_data(dataset = 'dataset_tissue.txt', clases = 'clases'):
    df = pd.read_csv(dataset, delimiter = ",")
    df.rename(columns={'Unnamed: 0':'ROW_NAME'}, inplace=True)
    col_num = df.columns.size
    df = df.T
    
    y_values = pd.read_csv(clases, delimiter = ",")
    y_values.rename(columns={'x':'tissue'}, inplace=True)
    y_list = y_values.iloc[:,-1].values.tolist()
    
    x_features = df.iloc[1:col_num,:]
    full_data = x_features.copy()
    full_data['tissue'] = y_list
    return full_data, x_features

#Reduciendo dimensiones con PCA, falta todavia
def reduce_dim(dataframe,componentes):
    x = dataframe.iloc[:,:-1]
    y = dataframe.iloc[:,-1]
    
    scaler = StandardScaler()
    scaler.fit(x)
    x_scaled = scaler.transform(x)
    pca = PCA(n_components=componentes)
    pca.fit(x_scaled)
    x_pca = pca.transform(x_scaled)