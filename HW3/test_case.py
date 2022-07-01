from topo import Topo
import numpy as np




def minDistance2(V,D_, N_):
    min = 1e7
    for v in range(V):
        if (D_[v] == -1):
            D_[v] = 1e7
        if (D_[v] != -1) and (D_[v] < min) and ([v] not in N_): # 
            min = D_[v]
            min_index = v
    return min_index

def minDistance(V,D_, N_):
    min = 1e7
    for v in range(V):
        if (D_[v] == -1):
            D_[v] = 1e7
        if (D_[v] != -1) and (D_[v] < min) and ([v] not in N_): # 
            min = D_[v]
    return D_, N_




def test(num):
    start = 0
    name = './test_case/'+str(num)+'.txt'
    out_name = './out/'+str(num)+'.txt'
    myTopo = Topo(name)

    N = np.zeros((myTopo.numNodes, 1)) ## 確定的點
    D = np.zeros((myTopo.numNodes, 1)) ## Cost current path
    p = np.zeros((myTopo.numNodes, 1)) ## previous current path

    for i in range(myTopo.numNodes):
        D[i] = -1
        p[i] = -1
        N[i] = -1

    #N[0] = start
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


    
    for cout in range(V):
        if cout == 0:
            u = 0
            D, N = minDistance(V,D,N)
            N[cout] = u
        if cout != 0:
            u = minDistance2(V,D, N)
            N[cout] = u
        for v in range(V):
            if (graph[u][v] > 0 and
                (v not in N) and
                D[v] > D[u] + graph[u][v]):
                D[v] = D[u] + graph[u][v]
                p[v] = u

    
    ### ans
    lines = []
    for i in range(1, myTopo.numNodes):
        #print(int(p[i]), ' --> ', i, ' cost = ', int(D[i]))
        s = str(int(p[i]))+'  -->  '+str(i)+'  cost =  '+str(int(D[i]))+'\n'
        lines.append(s)


    ## write csv
    with open(out_name, 'w') as f:
        for line in lines:
            f.write(line)
        
'''        
for cout in range(V):
    u = minDistance2(D, N)
    print(u)
    N[cout] = u
    for v in range(V):
        if (graph[u][v] > 0 and
            (v not in N) and
            D[v] > D[u] + graph[u][v]):
            D[v] = D[u] + graph[u][v]
            p[v] = u
    print(N)
    print(D)
'''
num = 0
test(num)

for i in range(100):
    num = i
    test(num)


