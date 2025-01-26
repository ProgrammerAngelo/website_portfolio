def merge_sort(arr):
    # This list will hold the steps of the merge sort process
    steps = []

    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr, steps

    # Divide the array into two halves
    mid = len(arr) // 2
    left, left_steps = merge_sort(arr[:mid])
    right, right_steps = merge_sort(arr[mid:])

    # Merge the two sorted halves
    merged = []
    i = j = 0

    # Merge the left and right lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are any elements left in either left or right, add them
    merged.extend(left[i:])
    merged.extend(right[j:])

    # Collect the merge process steps
    steps.append(f"Merging: {merged}")

    # Combine all steps and return
    steps = left_steps + right_steps + steps
    return merged, steps
