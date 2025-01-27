def partition(array, low, high, steps):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            # Log the swap
            steps.append(f"Swapped {array[i]} with {array[j]}: {array}")

    array[i + 1], array[high] = array[high], array[i + 1]
    # Log the pivot placement
    steps.append(f"Moved pivot {array[i + 1]} to the correct position: {array}")
    return i + 1

def quick_sort_algorithm(array, low, high, steps):
    if low < high:
        # Partition the array and log the process
        pi = partition(array, low, high, steps)

        steps.append(f"Partition at index {pi}, pivot is {array[pi]}: {array}")

        # Sort the left side of the pivot
        quick_sort_algorithm(array, low, pi - 1, steps)

        # Sort the right side of the pivot
        quick_sort_algorithm(array, pi + 1, high, steps)