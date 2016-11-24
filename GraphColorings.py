# Author: Andrew Jarombek
# Date: 11/17/2016
# Contains all of the algorithms for determining graph colorings

from Graph import Graph

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
        colors = list()
        for val in range(1, len(degreeList)):
            colors.append(val)

        coloredList = list()

        # Create a list of vertex saturation degrees
        # saturationDegreeList -> list((vertex,degree,saturationDegree,list(adjacentColors)))
        saturationDegreeList = list()
        for vertex in degreeList:
            satDegree = (vertex[0], vertex[1], 0, list())
            saturationDegreeList.append(satDegree)

    # Helper function for Brelaz algorithm to find the saturation degrees
    # of the unused vertices after a vertex is colored
    def findSaturationDegree(self, vertex, color, saturationDegreeList):
        adjacent = self.graph.neighborsOf(vertex)
        for saturation in saturationDegreeList:
            if saturation[0] in adjacent:
                if color not in saturation[2]:
                    saturation[3].append(color)
                    saturation[2] += 1

        saturationDegreeList = sorted(saturationDegreeList, reverse=True,
                                      key=lambda x: x[2])