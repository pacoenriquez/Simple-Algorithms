from random import randint

random_arr = []

for i in range(30):
    x = randint(1, 100)
    random_arr.append(x)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key

            j -= 1

    return arr


print(random_arr)
print(insertion_sort(random_arr))
