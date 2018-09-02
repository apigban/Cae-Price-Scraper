#!/usr/bin/env python3.7

import redis
import functools
import login_redis as lr
from datetime import datetime


redis_dump = redis.StrictRedis(
    host = lr.login['ip'],
    port = lr.login['port'],
    password = lr.login['password'],
    db = lr.login['db']
    )

def redisWrite(function_toWrite):
    """
    Writes to redis
    """

    @functools.wraps(function_toWrite)
    def wrapper_redisWrite(*args, **kwargs):
        value = function_toWrite(*args, **kwargs)       # run function wrapped
        value[3] = int(1000*value[3].timestamp())           #transform value[2] to timestamp to milliseconds and to type int
        print(value)
        return value

    #redis_dump.rpush('',value)
    return wrapper_redisWrite
