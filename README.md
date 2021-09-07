# CeleryTest
Simple program storing current time on Redis  
It uses Celery for pushing the task on tasks queue  
Using Redis as database  
Time will be stored as value of 'crTime' key in redis 

# how to run
Install **Redis** from redis.io  
Install **Celery** and **Redis** python libaries using :
```
pip install celery
pip install redis
```
Execute the following commands in 3 different terminals :
```
celery -A task beat -l INFO  
redis-server  
celery -A task worker -l INFO
```
  
Execute the following command in **redis-cli.exe** to get the last stored value :
```
get crTime
```
