import random
import numpy as np

### Question 1 (warm-up: Erdos-Renyi random graphs)
### Create a function called rand_graph(p, n) that returns a new random graph 
### with n nodes numbered 0 to n−1 such that every different pair of nodes is 
### connected with probability p. Assume n>1, and 0≤p≤1.

def rand_graph(p, n):
    vertex = []
    for i in range(n):
        vertex.append(i)
    edge = [(i,j) for i in range(n) for j in range(i) if random.random() < p]
    
    myDict = {new_list: [] for new_list in range(n)}

    for (i,j) in edge:
        myDict[i].append(j)
        myDict[j].append(i)
      
    return myDict
    

if __name__ == "__main__":

    graph = rand_graph(0.4, 5)
    print(graph)
