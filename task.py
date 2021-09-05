from celery import Celery
import os
import redis
from datetime import datetime

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

r = redis.Redis()

app = Celery('tasks',broker="redis://localhost:6379/0")

@app.task
def setTime():
    ans = r.set('crTime' , datetime.now().strftime("%I:%M:%S%p"))
    print("Time is set")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "runme-every-ten-seconds": {
    "task": "task.setTime",
    "schedule": 10.0
    }
}