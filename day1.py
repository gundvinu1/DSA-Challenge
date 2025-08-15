def sortColors(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Test Cases
print(sortColors([0, 1, 2, 1, 0, 2, 1, 0]))  # [0, 0, 0, 1, 1, 1, 2, 2]
print(sortColors([2, 2, 2, 2]))              # [2, 2, 2, 2]
print(sortColors([0, 0, 0, 0]))              # [0, 0, 0, 0]
print(sortColors([1, 1, 1, 1]))              # [1, 1, 1, 1]
print(sortColors([2, 0, 1]))                 # [0, 1, 2]
print(sortColors([]))                        # []
