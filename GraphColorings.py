# Author: Andrew Jarombek
# Date: 11/17/2016
# Contains all of the algorithms for determining graph colorings

from Graph import Graph
from random import randint

class GraphColorings(object):

    def __init__(self, vertexSet, edgeSet):
        self.graph = Graph(vertexSet, edgeSet)

    # Graph Coloring Algorithm #1 - Welsh-Powell
    # Step 1: All vertices are sorted by decreasing degree into a list V
    # Step 2: Have a list of colors ordered on a list C
    # Step 3: Color v1 the first vertex in V, c1 the first color in list C
    # Step 4: For every vertex not adjacent to v1 color it c1
    # Step 5: Repeat steps 3 and 4 on the remaining non-colored vertices with a
    # new color until the whole graph is colored
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

    # Graph Coloring Algorithm #2 - Brelaz
    # Step 1. Arrange the vertices by decreasing order of degrees.
    # Step 2. Have a list of colors numbered 1 through n.
    # Step 3. Color a vertex of maximum degree with color 1.
    # Step 4. Choose an uncolored vertex with maximum saturation degree. If there is a
    # tie, choose an uncolored vertex with the largest possible degree.
    # Step 5. Color the vertex with the least possible (lowest numbered) color.
    # Step 6. Stop if all vertices are colored, otherwise return to Step 4.
    def brelaz(self):
        degreeSet = self.graph.vertexDegreeSet()

        # degreeList -> list((vertex,degree))
        degreeList = list(degreeSet)

        # Sort the list of tuples using a lambda function
        degreeList = sorted(degreeList, reverse=True,
                            key=lambda x: x[1])

        # Create a list of potential colors
        colors = []
        for val in range(0, len(degreeList) - 1):
            colors.append(val)

        coloredList = list()

        # Add the vertex with highest degree to the colored list
        coloredVertex = (degreeList[0][0], 0)
        coloredList.append(coloredVertex)
        degreeList.pop(0)

        # Create a list of vertex saturation degrees
        # saturationDegreeList -> list((vertex,degree,saturationDegree,list(adjacentColors)))
        saturationDegreeList = []
        for vertex in degreeList:
            satDegree = (vertex[0], vertex[1], 0, [])
            saturationDegreeList.append(satDegree)

        # Update the saturationDegreeList for the first colored vertex
        saturationDegreeList = self.findSaturationDegree(coloredVertex[0], 0, saturationDegreeList)

        while len(saturationDegreeList) is not 0:
            vertex = saturationDegreeList.pop(0)
            usedColors = vertex[3]
            for color in colors:
                if usedColors and color not in usedColors:
                    coloredVertex = (vertex[0], color)
                    coloredList.append(coloredVertex)
                    saturationDegreeList = self.findSaturationDegree(vertex[0], color, saturationDegreeList)
                    break

        return coloredList

    # Helper function for Brelaz algorithm to find the saturation degrees
    # of the unused vertices after a vertex is colored
    def findSaturationDegree(self, vertex, color, saturationDegreeList):
        adjacent = self.graph.neighborsOf(vertex)
        index = 0
        for saturation in saturationDegreeList:
            if saturation[0] in adjacent:
                if color not in saturation[3]:
                    satDegList = saturation[3]
                    satDegList.append(color)
                    satDeg = saturation[2] + 1
                    saturationDegreeList[index] = (saturation[0], saturation[1], satDeg, satDegList)
            index += 1

        # Sort the Saturation Degree List by Saturation Degree With Degree as the tiebreaker
        saturationDegreeList = sorted(saturationDegreeList, reverse=True,
                                      key=lambda x: (x[2], x[1]))
        return saturationDegreeList

    # Graph Coloring Algorithm #3 - DLF
    # Every vertex has 3 parameters:
    # 1. The degree of the vertex deg(v)
    # 2. A random value which is generated locally and independently rndvalue(v)
    # 3. A list of forbidden colors that have been used by adjacent vertices
    # usedcolor(v) - initially is empty
    # Within each round every uncolored vertex v follows the same 5 steps
    # 1. Choose parameter rndvalue(v) uniformly distributed on[0…1].
    # 2. Send to all of the neighboring vertices deg(v) rndvalue(v) and the
    # first legal color (not on the list of v’s forbidden colors)
    # 3. Compare the parameters of v to the parameters of its neighbors to see
    # which vertex has the highest priority
    # 4. If vertex v’s proposed color does not clash with proposals from its neighbors or
    # if v has the highest priority among its neighbors keep the proposed color on v, send
    # message to the neighbors and stop.
    # 5. If not update the list usedcolor(v).
    def DLF(self):
        degreeSet = self.graph.vertexDegreeSet()

        # degreeList -> list((vertex,degree))
        degreeList = list(degreeSet)

        # vertexParamList -> list((vertex,degree,random,list(usedColors)))
        vertexParamList = []

        # populate the vertexParamList
        for vertex in degreeList:
            random = randint(1,10)
            usedColors = []
            vertexParam = (vertex[0], vertex[1], random, usedColors)
            vertexParamList.append(vertexParam)

        # Sort the list of tuples using a lambda function
        # Sorted by Degree with the Random Number as a tiebreaker
        vertexParamList = sorted(vertexParamList, reverse=True,
                                 key=lambda x: (x[1], x[2]))

        # Create a list of potential colors
        colors = []
        for val in range(0, len(degreeList) - 1):
            colors.append(val)
