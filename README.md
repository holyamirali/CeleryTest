# CeleryTest
a simple program storing current time on Redis  
it uses Celery for pushing the task on tasks queue  
using Redis as message broker  
time will be stored as value of 'crTime' key in redis 

# how to run
install Redis from redis.io, install Celery and Redis python libaries using pip
execute the following commands in 3 different terminals :  
celery -A task beat -l INFO  
redis-server  
celery -A task worker -l INFO
  
execute the following command in redis-cli.exe to get the last stored value :  
get crTime
