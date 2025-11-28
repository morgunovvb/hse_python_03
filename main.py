def sum_distance(from_num, to_num):
    if from_num < to_num:
        return sum(range(from_num, to_num + 1))
    else:
        return sum(range(to_num, from_num + 1))


num_1 = int(input())
num_2 = int(input())

print(sum_distance(num_1, num_2))
