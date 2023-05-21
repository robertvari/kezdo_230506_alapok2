import time, random, queue, threading
from my_functions.get_all_files import get_all_files

root = r"D:\Work\_PythonSuli\kezdo_230506\my_photos"
files = []
get_all_files(root, files)

# create job queue
job_queue = queue.Queue()
for i in files:
    job_queue.put(i)

def worker():
    while not job_queue.empty():
        next_job = job_queue.get()
        print(f"Converting {next_job}")
        time.sleep(random.randint(3, 10))
        print(f"Convert finished: {next_job}")
        job_queue.task_done()

for _ in range(6):
    t = threading.Thread(target=worker)
    t.start()