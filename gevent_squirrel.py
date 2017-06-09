import time
from gevent.pool import Pool
from gevent import monkey

from utils import *
from websites import *

# Note that you can spawn many workers with gevent since the cost of creating and switching is very low
NUM_WORKERS = 4

#Monkey patch socket module for HTTP requests
monkey.patch_socket()

start_time = time.time()

pool = Pool(NUM_WORKERS)
for address in WEBSITE_LIST:
	pool.spawn(check_website, address)

#Wait for stuff to finish
pool.join()

end_time = time.time()

print 'Time for GreenSquirrel=%ssecs'%(end_time-start_time)


# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://netflix.com returned status code=405
# WARNING:root:Website http://bing.com returned status code=405
# Time for GreenSquirrel=7.14988994598secs
