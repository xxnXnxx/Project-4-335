import heapq

def networkDelayTime(times, n, k):
    # i create an adjacency list for the graph
    adj_list = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        adj_list[u].append((v, w))

    # and distance array initialized to infinity
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    # and priority queue for Dijkstra's algorithm
    pq = [(0, k)]  # (time, node)

    while pq:
        time, node = heapq.heappop(pq)

        # Explore all neighbors
        for neighbor, weight in adj_list[node]:
            new_time = time + weight
            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    # then find the maximum time
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1

# Example usage
times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
print(networkDelayTime(times1, 4, 2))  # Output: 2

times2 = [[1, 2, 1]]
print(networkDelayTime(times2, 2, 1))  # Output: 1

times3 = [[1, 2, 1]]
print(networkDelayTime(times3, 2, 2))  # Output: -1
