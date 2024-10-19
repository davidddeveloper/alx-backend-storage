#!/usr/bin/env python3
"""
    exercise: different redis exercises

"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.lpush(f"{method.__qualname__}:inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.lpush(f"{method.__qualname__}:outputs", str(result))

    return wrapper


class Cache:
    """
        Represents a Redis Cache

    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
