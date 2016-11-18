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
        usedColors = 0

        # Continue to assign colors while the degreeList isn't empty
        while len(degreeList) != 0:

            # Always add the first item in the degreeList to an unused color
            largestDegree = degreeList[0]
            colored = (largestDegree[0], usedColors)
            coloredList.append(colored)
            degreeList.remove(largestDegree)

            # Go through all vertices in the degree list and look for adjacent
            # vertices with colorings matching the one we wish to apply.  If no
            # match is found, we can apply the color and remove the vertex from
            # the degreeList
            for v in degreeList:
                match = False
                adjacent = self.graph.neighborsOf(v[0])
                for cv in coloredList:
                    if cv[0] in adjacent and cv[1] is usedColors:
                        # If there is a match set match to true and stop
                        # searching for matches
                        match = True
                        break
                if not match:
                    colored = (v[0], usedColors)
                    coloredList.append(colored)
                    degreeList.remove(v)

            # All vertices checked, move to the next color
            usedColors += 1

        return coloredList

    # Graph Coloring Algorithm #1 - Welsh-Powell
    def brelaz(self):
        degreeSet = self.graph.vertexDegreeSet()
        degreeList = list(degreeSet)

        # Sort the list of tuples using a lambda function
        degreeList = sorted(degreeList, reverse=True,
                            key=lambda x: x[1])