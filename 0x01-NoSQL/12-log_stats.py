#!/usr/bin/env python3
"""
The python scrrip provides some script about
Nginx stored in MongoDB

atabase: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method =
["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
(see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip
"""


import pymongo
from pymongo import MongoClient

def log_nginx_stats(mongo_collection):
    """Provides some stats about Nginx logs"""
    print(f"{mongo_collection.estimated_document.count()} logs")
