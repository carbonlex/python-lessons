mylist = [10, 12 ,13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]

def binary_search(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) //2
        if search == mylist[mid]:
            return mid
        elif search < mylist[mid]:
            return binary_search(mylist, search, start, mid - 1)
        else:
            return binary_search(mylist, search, mid + 1, stop)


search = 10
start = 0
stop = len(mylist)


x = binary_search(mylist, search, start, stop)


if x == False:
    print("Item ", search, "Not Found")
else:
    print("Item ", search, "Found at Index ", x)

