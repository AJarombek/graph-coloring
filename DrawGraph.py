# Author: Andrew Jarombek
# Date: 11/25/2016
# Draws the Graphs using Matplotlib and Networkx

from GraphColorings import GraphColorings
import matplotlib.pyplot as plt
import networkx as nx

class DrawGraph(object):

    def __init__(self, type):
        self.nxgraph = self.generate(type)
        self.graph = GraphColorings(self.nxgraph.nodes(), self.nxgraph.edges())

    def generate(self, type):
        graphType = type[0]
        graphBlueprint = type[1]

        if graphType == 'Kn':
            return nx.complete_graph(int(graphBlueprint[1:]))

        elif graphType == 'Kn_n':
            if type(graphBlueprint[2]) is int:
                first = graphBlueprint[1:3]
                second = graphBlueprint[4:]
            else:
                first = graphBlueprint[1]
                second = graphBlueprint[3:]
            return nx.complete_bipartite_graph(first, second)

        elif graphType == 'Petersen':
            return nx.petersen_graph()

    def welshPowell(self):
        coloring = self.graph.welshPowell()
        self.color(coloring)

    def brelaz(self):
        coloring = self.graph.brelaz()
        self.color(coloring)

    def dlf(self):
        coloring = self.graph.DLF()
        self.color(coloring)

    def color(self, coloring):
        valMap = {}
        for v in coloring:
            valMap[v[0]] = (v[1] / 100)

        values = [valMap.get(node, 0.25) for node in self.graph.graph.vertices()]

        nx.draw(self.nxgraph, cmap=plt.get_cmap('jet'), node_color=values, pos=nx.circular_layout(self.nxgraph))
        plt.show()
