from pymongo import MongoClient
import config
'''
email: adwikara@bu.edu
'''

parameters = {'_id':1, 'pic' : '-1', 'object':'-1',  'class' : 'trash', 'percentage' : '100'}

#Connect to Mongo Atlas account
client = MongoClient(config.api_link)

#Creates a database called "sample"
db = client.sample

#Creates a collection called "testing"
mycol = client["test1"]
mycol2 = client["test2"]
mycol3 = client["testing"]

#Inserts information to the collection
result = db.test1.insert_one(parameters)
result = db.test2.insert_one(parameters)
result = db.testing.insert_one(parameters)
