import heapq  # TODO: added in the desc. order. heapq push is O(nlog(n)) and pop is O(1)


def k_largest_element(a, k):
    pq = []
    heapq.heapify(pq)
    for element in a:
        heapq.heappush(pq, element) # TODO: added in the desc. order.
        if len(pq)>k:
            heapq.heappop(pq)
    print(pq)


if __name__ == "__main__":
    k_largest_element([1, 23, 12, 9, 30, 2, 50], 3)
    k_largest_element( [11, 5, 12, 9, 44, 17, 2], 2)