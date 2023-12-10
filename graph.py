from itertools import combinations, groupby
import networkx as nx
import matplotlib.pyplot as plt
import random

class graph:
    def __init__(self):
        self.graph = nx.Graph()

    #Takes nodes and probability
    def random_connected_graph(self, node, prob):

        #Combination of edges between two nodes throughout list
        edges = combinations(range(node), 2)
        G = nx.Graph()
        #Adds nodes to the graph
        G.add_nodes_from(range(node))
        #if the prob <= 0 to zero there will not be an edge and return the graph
        #if prob >= 1 make an edge and return a 
        if prob <= 0:
            self.graph = G #Assigning the empty graph to self.graph
            return G
        if prob >= 1:
            self.graph = nx.complete_graph()
            #Every pair of node will be connected by an edge. The new graph will use the existing graph
            #Complete graph means that all pairs of distinct nodes have an edge connecting them.
            """return nx.complete_graph(node, create_using=G)"""
            return self.graph
        for _, node_edges in groupby(edges, key=lambda x: x[0]):
            node_edges = list(node_edges)
            random_edge = random.choice(node_edges)
            G.add_edge(*random_edge)
            #print(list(node_edges))
            for e in node_edges:
                if random.random() < prob:
                    G.add_edge(*e)
        """return G"""
        self.graph = G
        return self.graph

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)


    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


if __name__ == "__main__":
    g = graph()
    nodes = 150
    seed = random.randint(1,10)
    probability = 0.1
    G = g.random_connected_graph(nodes, probability)

    # Draw the graph after DFS traversal
    nx.draw(G, node_color='lightblue', 
            with_labels=True, 
            node_size=500)
    plt.show()
    g.DFS(0)