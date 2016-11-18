# Author: Andrew Jarombek
# Date: 11/17/2016
# Contains all of the algorithms for determining graph colorings

from Graph import Graph

class GraphColorings(object):

    def __init__(self, vertexSet, edgeSet):
        self.graph = Graph(vertexSet, edgeSet)

    # Graph Coloring Algorithm #1 - Welsh-Powell
    def welshPowell(self):
        degreeSet = self.graph.vertexDegreeSet()

        # Convert the Set to a list so it can be sorted
        degreeList = list(degreeSet)

        # Sort the list of tuples using a lambda function
        degreeList = sorted(degreeList, reverse=True,
                            key=lambda x: x[1])

        coloredList = list()
        colors = list()
        usedColors = 0
        colors.append(usedColors)

        while len(degreeList) != 0:
            for v in degreeList:
                if len(coloredList) == 0:
                    colored = (v[0], usedColors)
                    coloredList.append(colored)
                    degreeList.remove(v)
                else:
                    match = False
                    adjacent = self.graph.neighborsOf(v[0])
                    for cv in coloredList:
                        if cv[0] in adjacent:
                            match = True