import time

from utils import *
from websites import *

start_time=time.time()
for address in WEBSITE_LIST:
	check_website(address)

end_time = time.time()

print 'Time for Serial Squirel: %ssecs'%(end_time-start_time)


# WARNING:root:Website http://amazon.co.uk returned status code=503
# WARNING:root:Timeout expired for website http://really-cool-available-domain.com
# WARNING:root:Timeout expired for website http://another-really-interesting-domain.co
# WARNING:root:Website http://netflix.com returned status code=405
# WARNING:root:Website http://bing.com returned status code=405
# Time for Serial Squirel: 26.9407179356secs