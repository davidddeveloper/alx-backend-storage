#!/usr/bin/env python3
"""
    exercise: different redis exercises

"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
        Represents a Redis Cache

    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

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
