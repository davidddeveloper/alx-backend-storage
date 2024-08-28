#!/usr/bin/env python3
"""
    10-update_topics.py: changes all topics of a school document
    based on the name

"""


def update_topics(mongo_collection, name, topics):
    """
        change school topics base on the name
        name: the school name to update
        topics: list of topics 

    """
    mongo_collection.update({"name": name}, {"$set", {"topics": topics}}, True)
