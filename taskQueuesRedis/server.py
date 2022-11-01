import redis
import random


with redis.Redis() as redis_server:
    redis_server.lpush("queue", random.randint(0, 10))




# redis_server = redis.Redis()

# redis_server.close()