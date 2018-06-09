import numpy as np
import pandas as pd


class LogisticRegression:
    def __init__(self, alpha=0.001, max_iter=5000):
        self.alpha = alpha # скорость обучения
        self.max_iter = max_iter # количество итераций

    def fit(self, X_train, y_train):

        y_len = len(y_train) # считаем длину матрицы ответов
        X = X_train.copy() # копируем матрицу признаков
        X = np.insert(X_train, 0, 1, axis=1) # в матрицу Х добавлем столбец из нулей и из единиц

        theta = np.zeros(X.shape[1])

        for n in range(self.max_iter):
            z = np.dot(theta, X.T) # берем скалярное произведение теты на транспонированную матрицу признаков
            sigm = 1 / (1 + np.exp(-z)) # считаем коэф правдоподобия
            J_theta = np.dot((sigm - y_train), X) # считаем целевую функцию

            theta = theta - self.alpha * (1 / y_len) * J_theta  # обновление весов

        self.intercept = theta[0] # оценочные значения для теты 
        self.coef = theta[1:] # вектор оценок для теты

    def predict(self, X_test):
        prediction = []
        for i in X_test:
            z = self.intercept + np.sum(i * self.coef)
            sigm = 1 / (1 + np.exp(-z))

            if sigm >= 0.5:
                prediction.append(1)
            else:
                prediction.append(0)

        return prediction
