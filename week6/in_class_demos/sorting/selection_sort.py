def selection_sort(arr):
    # outer loop ensures we move up the array and place the items at the earliest position
    for index in range(len(arr)):
        current_index = index
        for next_index in range(index+1, len(arr)):
            if arr[next_index] < arr[current_index]:
                # remember the position of the smallest item found so far
                current_index = next_index
        # swap once per outer loop after the smallest item is found
        if current_index != index:
            arr[index], arr[current_index] = arr[current_index], arr[index]
    return arr

# Example usage: https://www.hackerearth.com/practice/algorithms/sorting/selection-sort/visualize/
print(selection_sort([64, 34, 25, 12, 22, 11, 90]))
