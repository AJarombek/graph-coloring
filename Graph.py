# Author: Andrew Jarombek
# Date: 11/17/2016
# Create a class which represents a Graph

class Graph(object):

    # constructor
    def __init__(self, vertexSet, edgeSet):
        self.vertexSet = vertexSet
        self.adjacencyMap = dict()
        for v in vertexSet:
            self.adjacencyMap[v] = set()
        for (u,v) in edgeSet:
            self.adjacencyMap[u].add(v)
            self.adjacencyMap[v].add(u)

    # Get the vertices in the graph
    def vertices(self):
        return self.adjacencyMap.keys()

    # Get the neighboring vertices of a certain vertex in the grpah
    def neighborsOf(self, v):
        return self.adjacencyMap[v]