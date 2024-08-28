#!/usr/bin/env python3
"""
    11-schools_by_topic.py: list of school having a specific topic

"""


def schools_by_topic(mongo_collection, topic):
    """
        returns the list of school having a specific topic
        mongo_collection: collection
        topic: the topic

    """
    return mongo_collection.find({"topics": topic})
