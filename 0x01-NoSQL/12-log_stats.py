#!/usr/bin/env python3
"""
    12-log_stats.py: script that provides some stats about Nginx logs
    stored in MongoDB

"""

from pymongo import MongoClient


def log():
    """log stats from mongodb"""

    client = MongoClient()  # establish connection
    db = client.logs  # database
    c_nginx = db.nginx  # nginx collection

    doc_count = c_nginx.count_documents({})

    # count logs for each method
    get_count = c_nginx.count_documents({"method": "GET"})
    post_count = c_nginx.count_documents({"method": "POST"})
    put_count = c_nginx.count_documents({"method": "PUT"})
    patch_count = c_nginx.count_documents({"method": "PATCH"})
    delete_count = c_nginx.count_documents({"method": "DELETE"})

    status_check_count = c_nginx.count_documents(
        {"path": "/status", "method": "GET"})

    # print statistic
    print(doc_count, 'logs')
    print("Methods:")
    print("\tmethod GET: {}".format(get_count))
    print("\tmethod POST: {}".format(post_count))
    print("\tmethod PUT: {}".format(put_count))
    print("\tmethod PATCH: {}".format(patch_count))
    print("\tmethod DELETE: {}".format(delete_count))
    print("{} status check".format(status_check_count))


if __name__ == '__main__':
    log()
