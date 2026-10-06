import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print(f"{end - start:.5f} seconds")
        return res
    return wrapper
@timer
def rm(data):
    if isinstance(data, dict):
        return {k: rm(v) for k, v in data.items() if rm(v) or v is False}
    elif isinstance(data, list):
        return [rm(item) for item in data if rm(item)]
    else:
        return data
print(rm([{'a': 1, 'b': 2, 'c': 3}, [[]], [1, []]]))