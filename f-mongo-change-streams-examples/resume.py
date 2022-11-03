

from bson.objectid import ObjectId
from datetime import date
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne, collection

client = MongoClient('mongodb+srv://user:pwd@claschda.da1ep.mongodb.net/test')
collection = client['db']['coll']

pipeline = [{
	    "$match": {
	        "operationType": { "$in": ["insert"] }
	    }
        # {'$match': {'fullDocument.value': {'$gt': 1000}}},
	}]

resume_token = {'_data': '8261E7EA4F000000012B022C0100296E5A1004F4C119E958124C4DA2863B14ADB7A6E946645F6964006461E7EA4FA6810BEF2E09D1850004'}

change_stream = collection.watch(
    pipeline,
    resume_after=resume_token)

print('stream opened')

for change in change_stream:
    print(change)