from gudhi import AlphaComplex, SimplexTree
from src.datasets import mnist
from pprint import pprint
import sys

print('Making alpha complex')
if len(sys.argv) > 1:
    ac = AlphaComplex(off_file=sys.argv[1])
else:
    ac = AlphaComplex(points=mnist(7))
print('And simplex tree')
simplex_tree = alpha_complex.create_simplex_tree(max_alpha_square=200000.0)
print(repr(simplex_tree))
pprint(dir(simplex_tree))
simplex_tree.get_filtration()
