import networkx as nx
import matplotlib.pyplot as plt

def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

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

# Find paths using DFS and BFS
start_station = "1st Ave"
goal_station = "9th Ave"
dfs_result = dfs_path(G, start_station, goal_station)
bfs_result = bfs_path(G, start_station, goal_station)

# Print DFS path
print("\nDFS explores as deep as possible before backtracking, often resulting in longer or non-optimal paths.")
print(f"DFS path from {start_station} to {goal_station}: {dfs_result}")

# Print BFS path
print("\nBFS explores all neighbors level by level, ensuring the shortest path in terms of edges.")
print(f"BFS path from {start_station} to {goal_station}: {bfs_result}")

# Visualize the graph
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, edge_color=colors, node_color="lightblue", node_size=2000, font_size=10)
plt.title("NYC Metro Network Graph")
plt.show()
