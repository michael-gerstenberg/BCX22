from datetime import date
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne, collection

import time
import sys

client = MongoClient('mongodb+srv://user:pwd@democluster.da1ep.mongodb.net/test?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=true')

collection = client['db']['coll']

change_stream = collection.watch([{
	    "$match": {
	        "operationType": { "$in": ["insert"] },
			# "updateDescription.updatedFields.name": "peter"
		#    "fullDocument.name": "pete"
	    }
	  }])

print('stream opened')

for change in change_stream:
    print(change)

    sys.stdout.write("\rDoing thing %i" % i)
    sys.stdout.flush()
    time.sleep(1)

