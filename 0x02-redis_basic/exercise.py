#!/usr/bin/env python3
"""
    exercise: different redis exercises

"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(fn.__qualname__)
        fn(self, *args, **kwargs)

    return wrapper


class Cache:
    """
        Represents a Redis Cache

    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        result = self._redis.get(key)
        if fn:
            result = fn(result)

        return result

    def get_str():
        pass

    def get_int():
        pass
