import schedule
import time
import os

print('Scheduler initialised')
schedule.every(1).minutes.do(lambda: os.system('scrapy crawl hackevents'))
schedule.every(1).minutes.do(lambda: os.system('scrapy crawl hackeventss'))
schedule.every(1).minutes.do(lambda: os.system('python mailauto.py'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while 1:
    schedule.run_pending()
    time.sleep(1)