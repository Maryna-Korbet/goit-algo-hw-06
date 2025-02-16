import networkx as nx
import matplotlib.pyplot as plt

# Create a graph for the New York Subway network 
G = nx.Graph()

# Add stations as an example 
stations = [
    "1st Ave", "3rd Ave", "5th Ave", "7th Ave", "9th Ave", "10th Ave", "14th St", 
    "23rd St", "34th St", "42nd St", "59th St", "72nd St", "86th St"
]

# Add edges to represent the subway lines 
edges = [
    ("1st Ave", "3rd Ave"), ("3rd Ave", "5th Ave"), ("5th Ave", "7th Ave"),
    ("7th Ave", "9th Ave"), ("9th Ave", "10th Ave"), ("10th Ave", "14th St"),
    ("14th St", "23rd St"), ("23rd St", "34th St"), ("34th St", "42nd St"),
    ("42nd St", "59th St"), ("59th St", "72nd St"), ("72nd St", "86th St")
]

# Add nodes and edges to the graph
G.add_nodes_from(stations)
G.add_edges_from(edges)

# Visualize the graph
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("Simplified New York Subway Network")
plt.show()

# Calculate and display the characteristics of the graph
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
degrees = [G.degree(node) for node in G.nodes]
num_vertices, num_edges, degrees

# Print the results
print(f"Number of stations (nodes): {num_vertices}")
print(f"Number of subway lines (edges): {num_edges}")
print(f"Degree of each station: {dict(zip(stations, degrees))}")