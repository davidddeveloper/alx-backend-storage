#!/usr/bin/env python3
"""
    8-all.py: list all documents in a collection

"""


def list_all(mongo_collection):
    """
        list documents in mongo_collection
        mongo_collection: collection

    """

    return mongo_collection.find()
