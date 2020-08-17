from random import randint

random_arr = []

for i in range(30):
    x = randint(1, 999)
    random_arr.append(x)

print(random_arr)


def radix_sort(arr):
    pos = 1
    while max(arr) // pos > 0:
        count_sort(arr, pos)
        pos *= 10
    return arr


def count_sort(arr, pos):
    count = []
    arr_b = []
    j = len(arr) - 1
    for i in range(10):
        count.append(0)
    for i in range(len(random_arr)):
        arr_b.append(0)
    for i in range(len(arr)):
        count[(arr[i] // pos) % 10] += 1
    for i in range(len(count)):
        if i > 0:
            count[i] += count[i - 1]
    for i in range(len(arr)):
        count[(arr[j] // pos) % 10] -= 1
        arr_b[count[(arr[j] // pos) % 10]] = arr[j]
        j -= 1
    for i in range(len(arr)):
        arr[i] = arr_b[i]


print(radix_sort(random_arr))
