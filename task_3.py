import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_all_paths(graph, start):
    return nx.single_source_dijkstra_path(graph, start)

# Define the metro lines with weights (time in minutes)
metro_lines = {
    "Red": [("1st Ave", "2nd Ave", 2), ("2nd Ave", "3rd Ave", 3), ("3rd Ave", "4th Ave", 2)],
    "Blue": [("5th Ave", "6th Ave", 2), ("6th Ave", "7th Ave", 3), ("7th Ave", "8th Ave", 2)],
    "Green": [("3rd Ave", "5th Ave", 4), ("5th Ave", "7th Ave", 3), ("7th Ave", "9th Ave", 2)],
}

# Colors for each line
line_colors = {
    "Red": "red",
    "Blue": "blue",
    "Green": "green",
}

# Create a graph
G = nx.Graph()

# Add weighted edges to the graph
edges = []
colors = []

for line, stations in metro_lines.items():
    for station1, station2, weight in stations:
        G.add_edge(station1, station2, weight=weight)
        edges.append((station1, station2))
        colors.append(line_colors[line])

# Choose a starting station
start_station = "1st Ave"

# Find shortest paths using Dijkstra's algorithm
shortest_paths = dijkstra_all_paths(G, start_station)

# Print the shortest paths from the start station
print(f"\nShortest paths from {start_station} using Dijkstra's algorithm:")
for station, path in shortest_paths.items():
    print(f"To {station}: {path}")

# Visualize the graph with weights
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))

# Draw the nodes and edges
nx.draw(G, pos, with_labels=True, edge_color=colors, node_color="lightblue", node_size=2000, font_size=10)
edge_labels = {(u, v): f"{d['weight']} min" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("NYC Metro Network Graph with Weighted Edges")
plt.show()