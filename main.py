def search(numbers, val):
    first = 0
    last = len(numbers)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if numbers[mid] == val:
            index = mid
        else:
            if val<numbers[mid]:
                last = mid -1
            else:
                first = mid +1
    return index
    
numbers = [10,20,30,40,50]
index = search(numbers, 20)

print(index)
