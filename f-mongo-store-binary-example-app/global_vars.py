from pymongo import MongoClient
import os

connStr = "mongodb+srv://user:pwd@democluster.da1ep.mongodb.net/?retryWrites=true&w=majority"

dbName = "database"
collName = "collection"
currDir = os.getcwd()  # get current directory
print('Current Directory: ' + currDir)
