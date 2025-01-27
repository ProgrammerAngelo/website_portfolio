def insertion_sort(arr):
    """
    Performs insertion sort on a list of integers and shows the sorting process step by step,
    explaining which elements are being swapped in each step.
    """
    steps = []  # To store the steps of sorting
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Show the array before insertion
        step_description = f"Step {i}: key = {key}, arr = {arr}"

        # Adding the description for the current step
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            step_description += f" -> Swapping {arr[j+1]} with {key}"

        arr[j + 1] = key
        
        # After insertion for this step
        step_description += f" -> After insertion, arr = {arr}"
        steps.append(step_description)
    
    return arr, steps