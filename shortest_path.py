import heapq

# Graph with approximate straight-line distances (weights in meters)
graph = {
    'User': {'Peacock': 100, 'White Tiger': 120},
    'Peacock': {'Elephant': 150, 'Lion': 250},
    'White Tiger': {'Elephant': 100},
    'Elephant': {'Lion': 100},
    'Lion': {'Snake': 130},
    'Snake': {'Monkey': 160},
    'Monkey': {}
}

def dijkstra(graph, start, goal):
    queue = [(0, start, [])]
    seen = set()
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in seen: continue
        path = path + [node]
        seen.add(node)
        if node == goal:
            return (cost, path)
        for neighbor, weight in graph.get(node, {}).items():
            heapq.heappush(queue, (cost + weight, neighbor, path))
    return float("inf"), []

# Example usage
start_node = "User"
goal_node = "Lion"
cost, path = dijkstra(graph, start_node, goal_node)

print("Shortest Path:", " → ".join(path))
print("Total Distance:", cost, "meters")
