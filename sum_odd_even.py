def even_odd(list1):
    sum_even = 0
    sum_odd = 0
    for i in range(len(list1)):
        if int(list1[i]) % 2 == 0:
            sum_even += int(list1[i])
        else:
            sum_odd += int(list1[i])

    return sum_even, sum_odd

list1 = input().split()

res = even_odd(list1)

print(res)