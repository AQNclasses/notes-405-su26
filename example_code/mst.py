from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import random


disconnected_graph = nx.watts_strogatz_graph(20,3,0.5,4)

connected_graph = nx.watts_strogatz_graph(20,3,0.5,5)

# Assign random unique integer weights to edges
# Input: NetworkX graph
# Output: NetworkX graph with same node and edge sets, randomized weights
# Operates in place as well as returning graph
def random_unique_weights(graph):
    E = graph.number_of_edges()
    weights = random.sample(range(1,2*E), E)
    for (u, v), w in zip(graph.edges, weights):
        graph[u][v]['weight'] = w

# Implement one of the MST algorithms we learned
# Input: NetworkX graph
# Output: NetworkX graph defining a minimum spanning tree (or forest if the
#         original graph has more than one component)
def mst(graph):

    return

# Run algo and visualize

graph = connected_graph # change for disconnected
graph = random_unique_weights(graph)
mst = mst(graph)

# Visualization
G = nx.Graph(graph)
pos = nx.spring_layout(G) # Layout for visualization

plt.figure(figsize=(8, 6))
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
plt.show()
