# create data

from datetime import date
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne, collection
import random
import time

client = MongoClient('mongodb+srv://user:pwd@claschda.da1ep.mongodb.net/test?authSource=admin&replicaSet=atlas-rk5bb1-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
collection = client['db']['coll']

while True:
    doc = {
        'machine_id': random.randint(1,10),
        'value': random.randint(1,1000)
    }
    collection.insert_one(doc)
    print(doc)
    time.sleep(1)
