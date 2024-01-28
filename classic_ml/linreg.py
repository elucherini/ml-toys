import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

from utils import Estimator, plot_regression_predictions


class LinReg(Estimator):
    def fit(self, X, y, epochs=1000):
        self.weights = np.random.rand(X.shape[1])
        self.bias = 0

        for _ in range(epochs):
            y_pred = self.infer(X)
            self.losses.append(mean_squared_error(y, y_pred))

            dw = (1 / X.shape[0]) * np.dot(X.T, y_pred - y)
            db = (1 / X.shape[0]) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db
            self.epochs += 1

        return self

    def infer(self, X):
        return np.dot(X, self.weights) + self.bias


def main():
    X, y = make_regression(n_samples=500, n_features=1, noise=15, random_state=49)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=49)

    estimator = LinReg()
    # "Fit" with random params
    y_pred_random = estimator.fit(X, y, epochs=0).infer(X)
    print("Initial MSE:", mean_squared_error(y, y_pred_random))

    # Train for 1000 epochs
    estimator.fit(X_train, y_train, epochs=1000)

    y_pred = estimator.infer(X_test)
    print("Final MSE:", mean_squared_error(y_test, y_pred))

    # Predict on whole dataset
    y_pred = estimator.infer(X)
    plot_regression_predictions(X, y, y_pred)


if __name__ == '__main__':
    main()