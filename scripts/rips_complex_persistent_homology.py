from gudhi import RipsComplex, SimplexTree
import gudhi
from src.datasets import mnist
from pprint import pprint
import sys

print('Making Rips complex')
if len(sys.argv) > 1:
    rc = RipsComplex(off_file=sys.argv[1])
else:
    rc = RipsComplex(points=mnist(7))
print('And simplex tree')
simplex_tree = rc.create_simplex_tree(max_dimension=10)

diag = simplex_tree.persistence()

print("betti_numbers()=")
print(simplex_tree.betti_numbers())

pprint(diag)
