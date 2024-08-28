#!/usr/bin/env python3
"""
    12-log_stats.py: script that provides some stats about Nginx logs
    stored in MongoDB

"""

from pymongo import MongoClient


client = MongoClient()  # client
db = client.logs  # database
c_nginx = db.nginx  # nginx collection

doc_count = c_nginx.count_documents({})

get_count = c_nginx.count_documents({"method": "GET"})
post_count = c_nginx.count_documents({"method": "POST"})
put_count = c_nginx.count_documents({"method": "PUT"})
patch_count = c_nginx.count_documents({"method": "PATCH"})
delete_count = c_nginx.count_documents({"method": "DELETE"})

status_check_count = c_nginx.count_documents({"path": "/status", "method": "GET"})

# print logs
print(doc_count)
print("Methods:")
print("    method GET: {}".format(get_count))
print("    method POST: {}".format(post_count))
print("    method PUT: {}".format(put_count))
print("    method PATCH: {}".format(patch_count))
print("    method DELETE: {}".format(delete_count))
print("{} status check".format(status_check_count))
