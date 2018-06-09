import numpy as np
import pandas as pd


class GDRegressor:
    def __init__(self, alpha=0.01, max_iter=100):
        self.alpha = alpha  # скорость обучения
        self.max_iter = max_iter  # количество итераций
        self.theta_history = [0] * self.max_iter  # сохраняются значения переменной self.theta
        self.cost_history = [0] * self.max_iter  # сохраняются значения целевой функции

    def fit(self, X_train, y_train):
        self.theta = np.matrix(X_train, dtype='float64') * 0  # создаём нулевую матрицу для значений теты, рамзером с выборку
        t = X_train.T
        m = y_train.size
        for i in range(1, self.max_iter):
            self.theta -= self.alpha * (t.dot(self.theta * X_train - y_train.reshape((m, 1)))) / m
            self.theta_history[i] = self.theta
            self.cost_history[i] = - 1 / m * np.sum(np.dot(y_train.T, np.log(X_train)) + np.dot((1 - y_train).T, np.log(1 - X_train)))
        self.coef_ = self.theta[1]
        self.intercept_ = self.theta[0]

        return self.coef_, self.intercept_

    def predict(self, X_test):
        m = X_test.size
        y = X_test.dot(self.theta.reshape(1, m))  # перемножаем выборку и вектор весов
        self.pred = y[0]

        return self.pred

    
def rmse(y_hat, y):
    m = y.size
    rmse = 0
    for i in range(m):
        rmse = ((sum(y_hat[i] - y[i]) ** 2) / m) ** 0.5
    return rmse


def r_squared(y_hat, y):
    m = y.size
    deter_coff = 0
    for i in range(m):
        deter_coff = 1 - (sum((y[i] - y_hat[i]) ** 2) / (sum((y[i] - y.mean()) ** 2)))
return deter_coff
