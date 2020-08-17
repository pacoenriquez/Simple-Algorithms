from random import randint

random_arr = []

for i in range(30):
    x = randint(1, 100)
    random_arr.append(x)


def merge_sort(arr):
    result = []
    if len(arr) < 2:
        return arr
    mid = int(len(arr) / 2)
    y = merge_sort(arr[:mid])
    z = merge_sort(arr[mid:])
    while len(y) > 0 or len(z) > 0:
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)

    return result


print(random_arr)
print(merge_sort(random_arr))
