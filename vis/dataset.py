from lib.datasets import mnist
from matplotlib import pyplot as plt

plt.figure()
for img in mnist(7):
    plt.imshow(img.reshape((28, 28)))
    plt.show()
