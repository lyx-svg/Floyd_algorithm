import numpy as np

def update(n, Path, A):
     for v in range(n):
          for i in range(n):
               for j in range(n):
                    if A[i][j]>A[i][v]+A[v][j]:
                         A[i][j] = A[i][v]+A[v][j]
                         Path[i][j] = v
     return Path


def floyd(u, v, Path):
     if Path[u][v]==-1:
          print("%s ->> %s" % (u, v))
     else:
          floyd(u, Path[u][v], Path)
          floyd(Path[u][v], v, Path)


Path = np.ones((4,4))
Path = -1*Path
Path = np.array(Path, dtype=int)
# print(Path)
inf = 1e9
A = [[0,5,inf,7],
     [inf,0,4,2],
     [3,3,0,2],
     [inf,inf,1,0]]
n = len(A)
Path = update(n, Path, A)
floyd(1, 0, Path)
# print(Path)