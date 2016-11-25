# Author: Andrew Jarombek
# Date: 11/25/2016
# Draws the Graphs using Matplotlib and Networkx

from Graph import Graph
from GraphColorings import GraphColorings
import matplotlib.pyplot as plt
import networkx as nx

# Create a K5 Graph
# Same as doing nx.complete_graph(5)
K5 = nx.Graph()
K5.add_nodes_from([1,5])
K5.add_edges_from([(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)])

vertices = set(K5.nodes())
edges = set(K5.edges())

K5Coloring = GraphColorings(vertices, edges)

# Create a Petersen Graph
# Peterson = nx.petersen_graph()

# vertices = set(Peterson.nodes())
# edges = set(Peterson.edges())

# PetersonColoring = GraphColorings(vertices, edges)

coloring = K5Coloring.welshPowell()
valMap = {}
for v in coloring:
    valMap[v[0]] = (v[1] / 100)

values = [valMap.get(node, 0.25) for node in K5Coloring.graph.vertices()]

nx.draw(K5, cmap=plt.get_cmap('jet'), node_color=values, pos=nx.circular_layout(K5))
plt.show()
