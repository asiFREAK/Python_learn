#8. Given an array of integers, find the subarray with the maximum sum.

def max_subaray_sum(arr):
    if not arr:
        return 0
    
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = max_subaray_sum(arr)
print("Maximum sum:", max_sum)  
