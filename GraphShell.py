# Author: Andrew Jarombek
# Date: 11/25/2016
# Interactive Shell for Using the Graph Coloring Algorithms

import re
from DrawGraph import DrawGraph


# Method for the command line shell to execute coloring algorithms
def shell():
    # Keep the shell running until the user specifically says to quit
    done = False
    print("Graph Shell 1.0 \nType 'help' for more information")
    while not done:
        command = input("> ")
        # Quit the shell command
        if command == 'quit':
            done = True
            continue

        # Display help infomation command
        elif command == 'help':
            help()
            continue

        # Execute coloring algorithm command
        elif command == 'exec':
            execute()
            continue

        else:
            print("Invalid Command")
            continue
    print("Goodbye!")


# Method for executing coloring graph algorithms
def execute():
    # Fist pick a specific graph to execute the algorithms on
    graph = pickGraph()
    if graph is None:
        return

    # Second pick the algorithm you want to use
    algorithm = pickAlgorithm()
    if algorithm is None:
        return

    # Create an instance of the graph using DrawGraph
    drawgraph = DrawGraph(graph)

    # If the user selects all algorithms iterate through them
    if algorithm == 'all':
        drawgraph.welshPowell()
        next()
        drawgraph.brelaz()
        next()
        drawgraph.dlf()
        return

    # Otherwise execute that specific algorithm
    elif algorithm == 'welshpowell':
        drawgraph.welshPowell()
        return

    elif algorithm == 'brelaz':
        drawgraph.brelaz()
        return

    elif algorithm == 'dlf':
        drawgraph.dlf()
        return


# Helper function to ask the user if they would like to continue
def next():
    while True:
        command = input("Type 'next' to continue:")
        if command == 'next':
            return


# Function for picking a graph type
def pickGraph():
    graph = input("Pick a Graph Type:")

    # Once submitted make sure it is a valid graph
    valid = validGraph(graph)

    # Command for the help information
    if graph == 'help':
        help(location="exec")
        return pickGraph()

    # Command to go back to the main shell
    elif graph == 'back':
        return None

    # Otherwise check if the valid submitted is valid
    # If it is valid return it
    elif valid:
        return valid

    # Otherwise display error message saying it is invalid and let the user try again
    else:
        print("Invalid Graph.")
        return pickGraph()


# Function to check whether the graph submitted by the user is valid
def validGraph(graph):
    # Valid regular expressions for matching
    Knregex = "^K\d{1,2}$"
    Kn_nregex = "^K\d{1,2}_\d{1,2}$"
    petersenregex = "^Petersen$"

    # Try to match the regular expressions
    matchKn = re.match(Knregex, graph, re.I)
    matchKn_n = re.match(Kn_nregex, graph, re.I)
    matchPetersen = re.match(petersenregex, graph, re.I)

    # If there is a valid match, return the graphType and graphBlueprint
    if matchKn:
        return ['Kn', graph]
    elif matchKn_n:
        return ['Kn_n', graph]
    elif matchPetersen:
        return ['Petersen', graph]
    else:
        return None


# Function to pick a coloring algorithm
def pickAlgorithm():
    algorithm = input("Pick an Algorithm:").lower()

    # Command for the help information
    if algorithm == 'help':
        help(location="exec")
        return pickAlgorithm()

    # Command to go back to the main shell
    elif algorithm == 'back':
        return None

    # If a valid algorithm is entered, return it
    elif algorithm == 'all' or algorithm == 'welshpowell' or algorithm == 'brelaz' or algorithm == 'dlf':
        return algorithm

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
