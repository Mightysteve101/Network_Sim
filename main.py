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
    plt.show()

    g.DFS(0)