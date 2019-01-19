#https://stackoverflow.com/questions/54261166/representation-of-a-number-as-a-sum-of-powers

from itertools import product

def is_sum_of_powers(X, n, N):
    largest_power = int(X ** (1/n))
    powers = [i**n for i in range(1, largest_power+1)]

    for cases in range(1, N+1):
        for i in product(*[powers]*cases):
            if sum(i) == X:
                return [int(j**(1/n)) for j in i]

    return 0

print(is_sum_of_powers(5, 3, 7)) # -> [1, 1, 1, 1, 1]
print(is_sum_of_powers(5, 2, 3)) # -> [1, 2]
print(is_sum_of_powers(7, 2, 2)) # -> 0
print(is_sum_of_powers(132, 2, 10)) # -> [2, 8, 8]
