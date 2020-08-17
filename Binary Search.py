from random import randint

arr = []
x = int(input("Enter number (1-100):"))


def create_arr():
    for i in range(100):
        i = randint(1, 100)
        arr.append(i)
    arr.sort()


def binary_search():
    first = 0
    last = len(arr) - 1
    found = False
    position = 0
    while first <= last and not found:
        mid = int((first + last) / 2)
        if arr[mid] == x:
            position = mid
            found = True
        else:
            if x < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        print("Element found at index " + str(position))
    else:
        print("Element not found")


create_arr()
print(arr)
print(len(arr))
binary_search()

