#Multithreaded Sorting (Shared Memory Model)
import threading

# 2: Global Data Setup
original_list = [7, 12, 19, 3, 18, 4, 2, 6, 15, 8]
sorted_global = [0] * len(original_list)

def sort_worker(start, end):
    # Sorting sublist of equal size
    sub = original_list[start:end]
    sub.sort()
    for i in range(len(sub)):
        original_list[start + i] = sub[i]

def merge_worker(mid):
    # Merging into the second global array
    left, right = original_list[:mid], original_list[mid:]
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_global[k] = left[i]; i += 1
        else:
            sorted_global[k] = right[j]; j += 1
        k += 1
    sorted_global[k:] = left[i:] if i < len(left) else right[j:]

# Execution logic for Question 5b
mid_pt = len(original_list) // 2
t1 = threading.Thread(target=sort_worker, args=(0, mid_pt))
t2 = threading.Thread(target=sort_worker, args=(mid_pt, len(original_list)))
t1.start(); t2.start()
t1.join(); t2.join()

t3 = threading.Thread(target=merge_worker, args=(mid_pt,))
t3.start(); t3.join()
print("Multithreaded Sort Result:", sorted_global)