import numpy as np

with open("Txt.txt") as f:
    a = np.array(list(f.read()))

_, cnt = np.unique(a, return_counts=True)
p = cnt / np.sum(cnt)

H = -np.sum(p * np.log2(p))

print(H)