import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme("talk")


def plot_regression_predictions(X, y, y_pred):
    # Recommend using one feature at a time
    plt.scatter(X, y)
    plt.plot(X, y_pred, color='black', label='pred')
    plt.legend()
    plt.show()


def plot_learning_curve(estimator):
    x = range(len(estimator.losses))
    plt.plot(x, estimator.losses)
    plt.show()


def get_confusion_matrix(y, y_pred):
    pass


class Estimator:
    def __init__(self, lr: int = 0.01) -> None:
        self.lr = lr
        self.epochs = 0
        self.weights = None
        self.bias = None
        self.losses = []