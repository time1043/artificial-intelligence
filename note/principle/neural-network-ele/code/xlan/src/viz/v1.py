import numpy as np
from matplotlib import pyplot as plt


def plot_size_toxicity(xs: np.ndarray, ys: np.ndarray, y_pre: np.ndarray | None = None):
    plt.title("Size-Toxicity Function", fontsize=12)
    plt.xlabel("Bean Size")
    plt.ylabel("Toxicity")
    plt.xlim(0, 1)
    plt.ylim(0, 1.2)

    plt.scatter(xs, ys)
    if y_pre is not None:
        plt.plot(xs, y_pre, color="r")

    plt.show()
