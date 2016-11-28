# Author: Andrew Jarombek
# Date: 11/25/2016
# Draws the Graphs using Matplotlib and Networkx

from GraphColorings import GraphColorings
import matplotlib.pyplot as plt
import networkx as nx
import re
import time

class DrawGraph(object):

    def __init__(self, type):
        self.nxgraph = self.generate(type)
        self.graph = GraphColorings(self.nxgraph.nodes(), self.nxgraph.edges())

    # Creates a graph instance with a given tuple (graphType, graphBlueprint)
    # The graph type is a String definition of the graph (Complete, Bipartite, etc.)
    # The Blueprint is a description of that type (the number of vertices in the graph)
    def generate(self, type):
        graphType = type[0]
        graphBlueprint = type[1]

        # Complete Graph
        if graphType == 'Kn':
            return nx.complete_graph(int(graphBlueprint[1:]))

        # Complete Bipartite Graph
        elif graphType == 'Kn_n':
            if re.match("^\d$", graphBlueprint[2]):
                first = int(graphBlueprint[1:3])
                second = int(graphBlueprint[4:])
            else:
                first = int(graphBlueprint[1])
                second = int(graphBlueprint[3:])
            return nx.complete_bipartite_graph(first, second)

        # Petersen Graph
        elif graphType == 'Petersen':
            return nx.petersen_graph()

    # Execute the welshPowell algorithm and record statistics
    def welshPowell(self):
        label = "Welsh and Powell Algorithm"
        print(label)
        start = time.time()
        coloring = self.graph.welshPowell()
        elapsed = time.time() - start
        print("Time Elapsed: ", elapsed)
        coloringNumber = self.getColoringNumber(coloring)
        print("Vertices: ", len(coloring))
        print("Coloring Number: ", coloringNumber)
        self.color(coloring, label)

    # Execute the brelaz algorithm and record statistics
    def brelaz(self):
        label = "Brelaz Algorithm"
        print(label)
        start = time.time()
        coloring = self.graph.brelaz()
        elapsed = time.time() - start
        print("Time Elapsed: ", elapsed)
        coloringNumber = self.getColoringNumber(coloring)
        print("Vertices: ", len(coloring))
        print("Coloring Number: ", coloringNumber)
        self.color(coloring, label)

    # Execute the dlf algorithm and record statistics
    def dlf(self):
        label = "DLF Algorithm"
        print(label)
        start = time.time()
        coloring = self.graph.DLF()
        elapsed = time.time() - start
        print("Time Elapsed: ", elapsed)
        coloringNumber = self.getColoringNumber(coloring)
        print("Vertices: ", len(coloring))
        print("Coloring Number: ", coloringNumber)
        self.color(coloring, label)

    # Helper method to get the coloring number of the graph from the algorithm result
    def getColoringNumber(self, coloring):
        colors = set()
        for color in coloring:
            colors.add(color[1])
        return len(colors)

    # Method to color the graph in a visual display
    def color(self, coloring, label):

        # Get a value map so each color has a distinct floating point value from 0 to 1.
        # This allows networkx to color the graph
        valMap = {}
        for v in coloring:
            valMap[v[0]] = (v[1] / 100)

        # Get a coloring map to use in the graph display
        coloringMap = {}
        for v in coloring:
            coloringMap[v[0]] = v[1]

        # Get distinct color values for each graph vertex coloring
        values = [valMap.get(node, 0.25) for node in self.graph.graph.vertices()]

        # Draw and show the graph
        nx.draw_networkx(self.nxgraph, cmap=plt.get_cmap('jet'), node_color=values,
                         pos=nx.circular_layout(self.nxgraph), labels=coloringMap,
                         font_color='w', font_weight='bold')
        plt.show()
