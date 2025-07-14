def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
            
    return None

testList = [1, 5, 7, 9, 11, 21] # for sorted array only!
result = binarySearch(testList, 5)

if result != None:
    print("Element found by index ->", result)
else:
    print("Element not found!")