# Binary search algorithm
def binarySearch(input, item):
    left = 0
    right = len(input) -1
    while left <= right:
        mid = (left + right)//2
        if(item == input[mid]) :
            return mid
        else :
            if(item < input[mid]) :
                right = mid - 1
            else :
                left = mid + 1
    return -1


list = [1, 2, 3, 4, 5, 6, 7, 8]
itemToSearch = 2
itemIndex = binarySearch(list, itemToSearch)
if(itemIndex != -1):
    print('Item found at index : ', itemIndex)
else:
    print('Item not found in the list')