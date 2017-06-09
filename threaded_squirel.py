import time
from Queue import Queue 
# from multiprocessing import Queue
import threading
from threading import Thread 

from utils import *
from websites import *

NUM_WORKERS = 4
task_queue = Queue()

def worker():
	#Constantly check the queue for addresses
	while True:
		address = task_queue.get()
		check_website(address)

		#Mark the processed task as done
		task_queue.task_done()

start_time = time.time()

#Create worker threads
threads = [Thread(target=worker) for _ in range(NUM_WORKERS)]

#Add the websites to the task queues
[task_queue.put(item) for item in WEBSITE_LIST]

#Start all the workers
[thread.start() for thread in threads]

#Wait for all the tasks in the queue to be processed
# [thread.join() for thread in threads]
task_queue.join()


end_time = time.time()
print 'Time for Threaded Squirrel: %ssecs'%(end_time-start_time)
# [thread.join() for thread in threads]

print threading.current_thread().name
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://bing.com returned status code=405
# WARNING:root:Website http://netflix.com returned status code=405
# Time for Threaded Squirrel: 4.43880105019secs

