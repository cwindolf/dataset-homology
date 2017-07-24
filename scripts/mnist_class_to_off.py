from src.off import write_off
from src.datasets import mnist
import sys

with open(sys.argv[2], 'w', encoding='ascii') as f:
    write_off(mnist(int(sys.argv[1])), f)