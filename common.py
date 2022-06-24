from functools import reduce
import math


# python3.8
def gcd(*numbers):
    return reduce(math.gcd, numbers)


def lcm(x, y):
    return x*y // math.gcd(x,y)


def construct_plist(n):
    prime_list = [1 for _ in range(n)]
    result = []
    for i in range(2, n):
        if prime_list[i]:
            result.append(i)
        else: continue
        for j in range(i,n,i):
            prime_list[j] = 0
    return result

