import time
from utils import check_website
from websites import WEBSITE_LIST

from celery import Celery 
from celery.result import ResultSet

app = Celery('celery_squirrel',
			 broker='redis://localhost:6379/0',
			 backend='redis://localhost:6379/0')


@app.task
def check_website_task(website):
	return check_website(website)

if __name__ == '__main__':
	start_time = time.time()

	#Using delay runs the task aysnc
	rs = ResultSet([check_website_task.delay(address) for address in WEBSITE_LIST])

	#Wait for the task to finish
	rs.get()

	end_time = time.time()

	print 'Celery Squirrel=',end_time-start_time