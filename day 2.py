# Approach 1: Using Sum Formula
def findMissingNumber(arr):
    n = len(arr) + 1   # Since one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


# Approach 2: Using XOR Trick
def findMissingNumberXOR(arr):
    n = len(arr) + 1
    xor_all = 0
    xor_arr = 0

    # XOR of numbers 1 to n
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR of array elements
    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr


# -----------------------
# Test Cases
# -----------------------
if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 5],             # Missing 3
        [2, 3, 4, 5],             # Missing 1
        [1, 2, 3, 4],             # Missing 5
        [1],                      # Missing 2
        list(range(1, 1000000))   # Missing 1000000
    ]

    print("---- Using Sum Formula ----")
    for arr in test_cases:
        print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")
        print("Missing Number:", findMissingNumber(arr))
        print()

    print("---- Using XOR Trick ----")
    for arr in test_cases:
        print(f"Input: {arr[:10]}{'...' if len(arr) > 10 else ''}")
        print("Missing Number:", findMissingNumberXOR(arr))
        print()
