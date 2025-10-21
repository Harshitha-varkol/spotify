import heapq  # for priority queue (min-heap)

def dijkstra(graph, start):
    # Initialize distances from start node to all others as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Min-heap priority queue → (distance, node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If found a shorter path to the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
