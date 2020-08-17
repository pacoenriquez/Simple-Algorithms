from random import randint

random_arr = []

for i in range(30):
    x = randint(1, 100)
    random_arr.append(x)


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        flag = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                flag = 1
        if flag == 0:
            break
    return arr


print(random_arr)
print(bubble_sort(random_arr))
