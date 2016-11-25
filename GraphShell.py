# Author: Andrew Jarombek
# Date: 11/25/2016
# Interactive Shell for Using the Graph Coloring Algorithms

def shell():
    done = False
    print("Graph Shell 1.0 \nType 'help' for more information")
    while not done:
        command = input("> ")
        if command == 'quit':
            done = True
            continue

        elif command == 'help':
            print("\n***** Commands *****")
            print("'quit' -> exit the application")
            print("'exec' -> execute a graph operation")
            print("\n***** Available Graphs *****")
            print("'Kn' -> A complete graph (ex. K30)")
            print("'Peterson' -> A peterson graph")
            print("'Kn_n' -> A complete bipartite graph (ex. K2_5)")
            print("\n***** Available Coloring Algorithms *****")
            print("'all' -> Go through all three algorithms")
            print("'WelshPowell' -> Welsh and Powell algorithm")
            print("'Brelaz' -> Brelaz algorithm")
            print("'DLF' -> DLF algorithm")
            continue

        elif command == 'exec':
            execute()
            continue

        else:
            print("Invalid Command")
            continue
    print("Goodbye!")

def execute():
    pass

if __name__ == '__main__':
    shell()