import time
import concurrent.futures  #pip install futures


from utils import *
from websites import *

NUM_WORKERS = 4
start_time = time.time()

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
	futures = {executor.submit(check_website, address) for address in WEBSITE_LIST}
	concurrent.futures.wait(futures)

end_time = time.time()
print 'TIme for futureSquirel: %ssecs' %(end_time-start_time)


# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://bing.com returned status code=405
# WARNING:root:Website http://netflix.com returned status code=405
# TIme for futureSquirel: 4.4736020565secs
