#5b
# git#Part B: Multithreaded Sorting Application
import threading

# Shared global data
data = [7, 12, 19, 3, 18, 4, 2, 6, 15, 8]  # Input from problem statement
sorted_final = [0] * len(data)

def sort_worker(start, end):
    """Sorting Thread: Sorts a sublist in-place."""
    sublist = data[start:end]
    sublist.sort()
    # Update global data with sorted sublist
    for i in range(len(sublist)):
        data[start + i] = sublist[i]

def merge_worker(mid):
    """Merging Thread: Merges two sorted halves into a final array."""
    left = data[:mid]
    right = data[mid:]
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_final[k] = left[i]
            i += 1
        else:
            sorted_final[k] = right[j]
            j += 1
        k += 1
    
    # Clean up remaining elements
    while i < len(left):
        sorted_final[k] = left[i]; i += 1; k += 1
    while j < len(right):
        sorted_final[k] = right[j]; j += 1; k += 1

def main():
    mid = len(data) // 2
    
    # 1. Spawn Sorting Threads
    t1 = threading.Thread(target=sort_worker, args=(0, mid))
    t2 = threading.Thread(target=sort_worker, args=(mid, len(data)))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    # 2. Spawn Merging Thread
    tm = threading.Thread(target=merge_worker, args=(mid,))
    tm.start()
    tm.join()
    
    print(f"Final Sorted List: {sorted_final}")
    print("Time Complexity: O(N log N)")

if __name__ == "__main__":
    main()