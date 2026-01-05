# Binary Search
# Items ordenados 
# Complexidade temporal -> O(log n)
# Complexidade espacial -> O(1)

def binary_search(nums, n):
    left = 0
    right = len(nums) - 1
    steps = 0
    
    while left <= right: 
        steps+=1
        mid = int((left + right)/2)
        
        if nums[mid] == n:
            print("steps: ", steps)
            return mid
        elif nums[mid] < n:
            left = mid + 1 
        else:
            right = mid - 1
    return -1

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

binary_search(d, 3)