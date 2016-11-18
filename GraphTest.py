# Author: Andrew Jarombek
# Date: 11/17/2016
# A test suite for the Graph class

from Graph import Graph

def test():

    # Create a Graph
    vertexSet = {1,2,3}
    edgeSet = {(1,2), (2,3)}
    graph = Graph(vertexSet, edgeSet)

if __name__ == '__main__':
    test()
