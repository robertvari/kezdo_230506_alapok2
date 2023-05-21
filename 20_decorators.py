import time, random

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


@temperature_logger
@my_timer
def worker1(min, max):
    print("Worker1 started...")
    time.sleep(random.randint(1, 4))
    print("Worker1 finished")
    return random.randint(min, max)


result = worker1(40, 1000)
print(result)