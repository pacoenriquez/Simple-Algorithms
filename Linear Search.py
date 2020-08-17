from random import randint

arr = []
x = int(input("Enter number (1-100):"))


def create_arr():
    for i in range(100):
        e = randint(1, 100)
        arr.append(e)


def linear_search():
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


create_arr()
print(arr)
print("Element found at index " + str(linear_search()))
