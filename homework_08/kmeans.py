import pandas as pd
import numpy as np
from copy import deepcopy
from random import sample

def distance(v1, v2, ax=1):
    return np.linalg.norm(v1 - v2, axis=ax) #считаем расстояние между точками и центроидами


class KMeans:
    def __init__(self, n_clusters, max_iter=500):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        n_samples = len(X)
        centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        centroids_old = np.zeros(centroids.shape)   # .shape - размер массива
        clusters = np.zeros(n_samples)  # матрица из нулей размером Х

        while True:
            for i in range(n_samples):
                distances = distance(X[i,], centroids)
                clusters[i] = distances.argmin()
            centroids_old = deepcopy(centroids)
            for k in range(self.n_clusters):
                centroids[k] = X[clusters == k,].mean(axis=0)   # сопоставляем центроид к кластеру
            error = distance(centroids, centroids_old, None)
            if (error >= 0) and (error <= 0.01):
                self.clusters = clusters.astype('int')  # принадлежность элемента к тому или иному кластеру
                self.centroids = centroids
                break

    def predict(self, y):
        y_unique = np.unique(y)  # выделяем кластеры
        y_unique_num = [i for i in range(len(np.unique(y)))]    # номера для кластеров
        n_samples = len(X)
        clusters = np.zeros(n_samples)  # матрица из нулей размером Х
        for k in range(n_samples): #кластерам присваиваются цифры вместо названий
            for j in range(self.n_clusters):
                if y[k][0] == y_unique[j]:
                    y[k] = y_unique_num[j]
            clusters[k] = y[k]
        centroids = X[np.random.choice(X.shape[0], self.n_clusters,
                                       replace=False)]   # X.shape[0] - строки
        centroids_old = np.zeros(centroids.shape)  # .shape - размер массива (длина массива по каждой оси)
        while True:
            centroids_old = deepcopy(centroids)
            error = distance(centroids, centroids_old, None)
            if error == 0:
                self.clusters = clusters.astype(int)
                self.centroids = centroids
return self.centroids, self.clusters
