import sys
from collections import deque

def read_input(filename):
    with open(filename, "r") as f:
        nums = list(map(int, f.read().split()))
    
    k = nums[0]
    m = nums[1]
    requests = nums[2:]
    
    if len(requests) != m:
        raise ValueError(f"Expected {m} requests, but got {len(requests)}")
    
    return k, m, requests

def fifo_misses(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for req in requests:
        if req in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(req)
            order.append(req)
        else:
            evicted = order.popleft()
            cache.remove(evicted)

            cache.add(req)
            order.append(req)

    return misses

def lru_misses(k, requests):
    cache = set()
    order = []
    misses = 0

    for req in requests:
        if req in cache:
            order.remove(req)
            order.append(req)
        else:
            misses += 1

            if len(cache) < k:
                cache.add(req)
                order.append(req)
            else:
                evicted = order.pop(0)
                cache.remove(evicted)

                cache.add(req)
                order.append(req)

    return misses

def optff_misses(k, requests):
    cache = set()
    misses = 0

    for i, req in enumerate(requests):
        if req in cache:
            continue

        misses += 1

        if len(cache) < k:
            cache.add(req)
        else:
            farthest_item = None
            farthest_next_use = -1

            for item in cache:
                try:
                    next_use = requests.index(item, i + 1)
                except ValueError:
                    next_use = float('inf')

                if next_use > farthest_next_use:
                    farthest_next_use = next_use
                    farthest_item = item

            cache.remove(farthest_item)
            cache.add(req)

    return misses

def main():
    if len(sys.argv) != 2:
        print("Usage: python src/main.py <input_file>")
        return
    
    filename = sys.argv[1]
    k, m, requests = read_input(filename)

    fifo = fifo_misses(k, requests)
    lru = lru_misses(k, requests)
    optff = optff_misses(k, requests)

    print(f"FIFO  : {fifo}")
    print(f"LRU   : {lru}")
    print(f"OPTFF : {optff}")

if __name__ == "__main__":
    main()