#!/usr/bin/env python3.7

import redis
import functools
import login_redis as lr
from datetime import datetime


rediscmd = redis.StrictRedis(
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
        #valid_product, error_status, time_stamp, requester, request_id  = function_toWrite(*args, **kwargs)       # run function wrapped

        commit_list = function_toWrite(*args, **kwargs)       # run function wrapped
        request_id = commit_list[4]


        print(f'commit_list: {commit_list}')
        #print(f'valid_product: {valid_product}')
        #print(f'error_status: {error_status}')
        #print(f'time_stamp: {time_stamp}')

        rediscmd.rpush(request_id, *commit_list)
        #return value

    return wrapper_redisWrite

def pull_redisvalue():

    total_messageQ = rediscmd.dbsize()
    keys = rediscmd.ke

    redis.dump.lrange(item)
