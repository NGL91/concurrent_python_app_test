Let's build an application that checks the uptime of websites. There are a lot of such solutions out there, the most well-known ones being probably Jetpack Monitor and Uptime Robot. The purpose of these apps is to notify you when your website is down so that you can quickly take action. Here's how they work:

The application goes very frequently over a list of website URLs and checks if those websites are up.
Every website should be checked every 5-10 minutes so that the downtime is not significant.
Instead of performing a classic HTTP GET request, it performs a HEAD request so that it does not affect your traffic significantly.
If the HTTP status is in the danger ranges (400+, 500+), the owner is notified.
The owner is notified either by email, text-message, or push notification.


Code get from https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612


Command line run with celery

>> celery worker -A celery_squirrel --loglevel=debug --concurrency=4
>> python2 celery_squirrel.py
