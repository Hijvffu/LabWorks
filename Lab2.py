import time
import functools


def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            return result
        finally:
            elapsed = time.perf_counter() - start
            print(f"[timing] {func.__name__} выполнилась за {elapsed:.6f} сек")
    return wrapper

@timing
def f1(n):
    k = 0
    for i in range(n):
        k += i ** 2
    return k

print(f1(10))
