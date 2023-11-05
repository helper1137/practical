def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Choose the last element as the pivot
    left = []
    right = []

    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    return quickSort(left) + [pivot] + quickSort(right)

# Driver code
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quickSort(arr)
print("Sorted array:", sorted_arr)

#method 2

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]  # Deterministic pivot (choose any element)
    left, right = [], []

    for element in arr[:-1]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Randomized pivot
    left, right = [], []

    for element in arr:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Deterministic QuickSort:", sorted_arr)

sorted_arr_random = randomized_quick_sort(arr)
print("Randomized QuickSort:", sorted_arr_random)
