import networkx as nx
import matplotlib.pyplot as plt

# Define the metro lines and their stations
metro_lines = {
    "Red": [("1st Ave", "2nd Ave"), ("2nd Ave", "3rd Ave"), ("3rd Ave", "4th Ave")],
    "Blue": [("5th Ave", "6th Ave"), ("6th Ave", "7th Ave"), ("7th Ave", "8th Ave")],
    "Green": [("3rd Ave", "5th Ave"), ("5th Ave", "7th Ave"), ("7th Ave", "9th Ave")],
}

# Colors for each line
line_colors = {
    "Red": "red",
    "Blue": "blue",
    "Green": "green",
}

# Create a graph
G = nx.Graph()

# Add nodes and edges to the graph
edges = []
colors = []

for line, stations in metro_lines.items():
    for station1, station2 in stations:
        G.add_edge(station1, station2)
        edges.append((station1, station2))
        colors.append(line_colors[line]) 

# Create a layout for the graph
pos = nx.spring_layout(G, seed=42)

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, edge_color=colors, node_color="lightblue", node_size=2000, font_size=10)

plt.title("NYC Metro Network Graph")
plt.show()

# Print the results
print(f"Number of stations (nodes): {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Degree of each station: {dict(zip(G.nodes, [G.degree(node) for node in G.nodes]))}")