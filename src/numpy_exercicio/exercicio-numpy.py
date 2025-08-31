
import numpy as np

_N = "\n"

mt = np.array([12,34,26,18,10])
print(mt)
print(type(mt))

mtInt = np.array([1,2,3])
mtFloat = np.float32(mtInt)

print(mtFloat)
print(type(mtFloat))

vazio = np.empty([3,2], dtype=int)

print("vazio")
print(vazio)
print(type(vazio))

diagonal = np.eye(5)
print("diagonal:", diagonal, sep=_N)

ale = np.random.rand(5)
print("Aleatórios:", ale, sep=_N)

ale2 = (10 * np.random.rand(3,4))
print("Aleatórios 3x4:", ale2, sep=_N)

# Semente
gnr = np.random.default_rng(1)
seed = gnr.random(3)
print("Semente:", seed)

# Unique
arr = np.array([12,11,12,11,13,15,20])
print("Normal:", arr, "unique:",np.unique(arr), sep=_N)
