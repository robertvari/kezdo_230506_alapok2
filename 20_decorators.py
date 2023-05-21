import time, random
from my_functions.decorators import my_timer, temperature_logger


@temperature_logger
@my_timer
def worker1(min, max):
    print("Worker1 started...")
    time.sleep(random.randint(1, 4))
    print("Worker1 finished")
    return random.randint(min, max)


result = worker1(40, 1000)
print(result)