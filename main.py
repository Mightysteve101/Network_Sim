import sys
import networkx as nx
import matplotlib.pyplot as plt
from graph import graph
import random

if __name__ == "__main__":
    g = graph()
    nodes = 150
    seed = random.randint(1,10)
    probability = 0.5
    G = g.random_connected_graph(nodes, probability)

    # Draw the graph after DFS traversal
    nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    with open('connectedGraph.txt', 'w') as f:
        sys.stdout = f
        print("Number of nodes", G.number_of_nodes(), file=f )
        print("Number of edges", G.number_of_edges(), file=f)
        #g.DFS(0)
        V = g.print_edges()
    plt.show()
