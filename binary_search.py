import numpy as np
def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, target, low, mid - 1)
        else:
            return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return -1
ls=[]
a=int(input('enter array length'))
for i in range(a):
    b=int(input())
    ls.append(b)
arr = np.sort(ls)
target = int(input('enter target value'))
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")
