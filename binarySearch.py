def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

testList = [1, 5, 7, 9, 11, 21, 77, 81, 101, 121, 125] # for sorted array only!
print("last index", len(testList) - 1)

result = binarySearch(testList, 101)

if result != None:
    print("Element found by index ->", result)
else:
    print("Element not found!")