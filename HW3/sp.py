from topo import Topo
import numpy as np

start = 0

myTopo = Topo('input.txt')

N = np.zeros((myTopo.numNodes, 1)) ## 確定的點
D = np.zeros((myTopo.numNodes, 1)) ## Cost current path
p = np.zeros((myTopo.numNodes, 1)) ## previous current path

for i in range(myTopo.numNodes):
    D[i] = -1
    p[i] = -1
    N[i] = -1

D[start] = 0
p[start] = start


# TODO: your codes here
graph = [[0 for column in range(myTopo.numNodes)]
          for row in range(myTopo.numNodes)]

for i in range(myTopo.numNodes):
    for j in range(myTopo.numNodes):
        if myTopo.links[i][j] > 0:
            graph[i][j] = myTopo.links[i][j]
#print(graph)

V = myTopo.numNodes


def minDistance2(D_, N_):
    min = 1e7
    for v in range(V):
        if (D_[v] == -1):
            D_[v] = 1e7
        if (D_[v] != -1) and (D_[v] < min) and ([v] not in N_): # 
            min = D_[v]
            min_index = v
    return min_index

def minDistance(D_, N_):
    min = 1e7
    for v in range(V):
        if (D_[v] == -1):
            D_[v] = 1e7
        if (D_[v] != -1) and (D_[v] < min) and ([v] not in N_): # 
            min = D_[v]
    return D_, N_

for cout in range(V):
    if cout == 0:
        u = 0
        D, N = minDistance(D,N)
        N[cout] = u
    if cout != 0:
        u = minDistance2(D, N)
        N[cout] = u
    for v in range(V):
        if (graph[u][v] > 0 and
            (v not in N) and
            D[v] > D[u] + graph[u][v]):
            D[v] = D[u] + graph[u][v]
            p[v] = u


for i in range(1, myTopo.numNodes):
    print(int(p[i]), ' --> ', i, ' cost = ', int(D[i]))
