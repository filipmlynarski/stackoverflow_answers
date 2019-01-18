from itertools import product

def is_sum_of_powers(X, n, N):
    largest_power = int(X ** .5)
    powers = [i**2 for i in range(1, largest_power+1)]

    for cases in range(1, N+1):
        for i in product(*[powers]*cases):
            if sum(i) == X:
                return [int(j**0.5) for j in i]

    return 0

print(is_sum_of_powers(5, 3, 7)) # -> [1, 2]
print(is_sum_of_powers(5, 2, 3)) # -> [1, 2]
print(is_sum_of_powers(7, 2, 2)) # -> 0
