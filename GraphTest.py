# Author: Andrew Jarombek
# Date: 11/17/2016
# A test suite for the Graph class

from Graph import Graph

def test():

    # Create a Graph
    vertexSet = {1,2,3}
    edgeSet = {(1,2), (2,3)}
    graph = Graph(vertexSet, edgeSet)

    # Inspect the Graph
    for v in graph.vertices():
        print(v, "->", graph.neighborsOf(v))

if __name__ == '__main__':
    test()
