import time

def my_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Process time: {time.time()-start_time}")

        return result

    return wrapper

def temperature_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 50:
            print(f"WARNING: Temperature is too high: {result}")

        return result

    return wrapper