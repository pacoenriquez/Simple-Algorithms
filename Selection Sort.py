from random import randint

random_arr = []

for i in range(30):
    x = randint(1, 100)
    random_arr.append(x)


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i

        for j in range(i + 1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        temp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = temp

    return arr


print(random_arr)
print(selection_sort(random_arr))
