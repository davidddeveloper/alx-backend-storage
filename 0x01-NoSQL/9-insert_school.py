#!/usr/bin/env python3
"""
    9-insert_school.py: Insert a new document in a collection
    base on kwargs

"""


def insert_school(mongo_collection, **kwargs):
    """
        Insert a new document
        **kwargs: the doc to be inserted

        Return: the id of the inserted doc

    """
    return mongo_collection.insert_one(kwargs).inserted_id
