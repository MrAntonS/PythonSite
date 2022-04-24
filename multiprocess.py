from time import perf_counter, time


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True


x = perf_counter()
num = 0
for i in range(2, 2500001):
    num += is_prime(i)
print(perf_counter() - x)
print(num)