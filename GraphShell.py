# Author: Andrew Jarombek
# Date: 11/25/2016
# Interactive Shell for Using the Graph Coloring Algorithms

import re

def shell():
    done = False
    print("Graph Shell 1.0 \nType 'help' for more information")
    while not done:
        command = input("> ")
        if command == 'quit':
            done = True
            continue

        elif command == 'help':
            help()
            continue

        elif command == 'exec':
            execute()
            continue

        else:
            print("Invalid Command")
            continue
    print("Goodbye!")

def execute():
    graph = pickGraph()
    if graph is None:
        return

    algorithm = pickAlgorithm()
    if algorithm is None:
        return


def pickGraph():
    graph = input("Pick a Graph Type:")
    valid = validGraph(graph)

    if graph == 'help':
        help(location="exec")
        return pickGraph()

    elif graph == 'back':
        return None

    elif valid:
        return graph

    else:
        print("Invalid Graph.")
        return pickGraph()

def validGraph(graph):
    Knregex = "^K\d{1,2}$"
    Kn_nregex = "^K\d{1,2}_\d{1,2}$"
    petersenregex = "^Petersen$"

    matchKn = re.match(Knregex, graph, re.I)
    matchKn_n = re.match(Kn_nregex, graph, re.I)
    matchPetersen = re.match(petersenregex, graph, re.I)

    if matchKn:
        return ['Kn', graph]
    elif matchKn_n:
        return ['Kn_n', graph]
    elif matchPetersen:
        return ['Petersen', graph]
    else:
        return None

def pickAlgorithm():
    algorithm = input("Pick an Algorithm:").lower()

    if algorithm == 'help':
        help(location="exec")
        return pickAlgorithm()

    elif algorithm == 'back':
        return None

    elif algorithm == 'all':
        return 0

    elif algorithm == 'welshpowell':
        return 1

    elif algorithm == 'brelaz':
        return 2

    elif algorithm == 'dlf':
        return 3

    else:
        print("Invalid Algorithm.")
        return pickAlgorithm()

# Function displays help messages
def help(location=None):
    print("\n***** Commands *****")
    if location is None:
        print("'quit' -> exit the application")

    print("'exec' -> execute a graph operation")

    if location == 'exec':
        print("'back' -> stop the graph execution")

    print("\n***** Available Graphs *****")
    print("'Kn' -> A complete graph (ex. K30)")
    print("'Petersen' -> A petersen graph")
    print("'Kn_n' -> A complete bipartite graph (ex. K2_5)")
    print("\n***** Available Coloring Algorithms *****")
    print("'all' -> Go through all three algorithms")
    print("'welshpowell' -> Welsh and Powell algorithm")
    print("'brelaz' -> Brelaz algorithm")
    print("'dlf' -> DLF algorithm")

if __name__ == '__main__':
    shell()