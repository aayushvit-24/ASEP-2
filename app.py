from flask import Flask, request, jsonify
import heapq

app = Flask(__name__)

# Graph: manually map paths with rough distances (adjust as needed)
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
        cost, node, path = heapq.heappop(queue)
        if node in seen:
            continue
        path = path + [node]
        seen.add(node)
        if node == goal:
            return cost, path
        for neighbor, weight in graph.get(node, {}).items():
            heapq.heappush(queue, (cost + weight, neighbor, path))
    return float('inf'), []

@app.route("/shortest-path", methods=["POST"])
def shortest_path():
    data = request.get_json()
    start = data.get("start", "User")
    end = data.get("end")
    cost, path = dijkstra(graph, start, end)
    return jsonify({"path": path, "distance": cost})

if __name__ == "__main__":
    app.run(debug=True)
