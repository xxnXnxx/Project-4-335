import heapq

def minLaptops(start_end):
    # i sort the intervals by start time
    start_end.sort(key=lambda x: x[0])
    
    # and priority the queue to track end times of ongoing laptop rentals
    heap = []
    laptops_needed = 0

    for start, end in start_end:
        # If the laptop is available (end time <= current start), free it
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add the current interval's end time to the heap
        heapq.heappush(heap, end)
        
        # Update the maximum number of laptops needed
        laptops_needed = max(laptops_needed, len(heap))

    return laptops_needed

# input usage here
start_end = [
    [0, 2], [1, 4], [4, 6], [0, 4], [7, 8], [9, 11], [3, 10]
]
print(minLaptops(start_end))  # and this is the sample output: 3
