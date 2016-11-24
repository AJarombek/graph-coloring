# Author: Andrew Jarombek
# Date: 11/17/2016
# A test suite for the Graph class

from Graph import Graph
from GraphColorings import GraphColorings

def test():

    # Create a Graph
    vertexSet = {1,2,3}
    edgeSet = {(1,2), (2,3)}
    graphcoloring = GraphColorings(vertexSet, edgeSet)

    # Inspect the Graph
    print("Adjacent Vertices:")
    for v in graphcoloring.graph.vertices():
        print(v, "->", graphcoloring.graph.neighborsOf(v))

    # Test the Welsh-Powell Graph Coloring Algorithm
    coloring = graphcoloring.welshPowell()
    print("Welsh-Powell Graph Coloring:")
    for v in coloring:
        print(v[0], "-->", v[1])

    # Test the Brelaz Graph Coloring Algorithm
    coloring = graphcoloring.brelaz()
    print("Brelaz Graph Coloring:")
    for v in coloring:
        print(v[0], "-->", v[1])


if __name__ == '__main__':
    test()
