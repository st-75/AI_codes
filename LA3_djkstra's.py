import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    predecessors = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
           
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def shortest_path(predecessors, start, end):
   
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    return path

def main():
    
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))

    graph = {}

    for _ in range(num_edges):
        start, end, weight = input("Enter start node, end node, and weight separated by space: ").split()
       
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = int(weight)
        graph[end][start] = int(weight)  
  
    start_node = input("Enter the start node: ")
  
    shortest_distances, predecessors = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node + ":")
    for node, distance in shortest_distances.items():
        print("To node", node + ":", distance)

if __name__ == "__main__":
    main()
