from pymongo import MongoClient 
from bson import ObjectId

## Mongo DB
client = MongoClient() # creating a MongoClient object 
client = MongoClient("mongodb://localhost:27017/") # connecting with the portnumber and host 

# Database
database = client["recipe-manager-db"] # Main db
# Database Collections
users = database["users"]
recipes = database["recipes"] 
ingredients = database["ingredients"] 


def GetListCollections():
    """List all collections in the database"""
    for coll in database.list_collection_names():
        print(coll)

def GetCollectionData(coll):
    """Get all data in the given collection"""
    collection = database[coll]
    data = []
    for item in collection.find():
        data.append(item)
    return data

def DropDataCollection(coll):
    """Drop given collection"""
    collection = database[coll]
    collection.drop()

def DeleteDataCollection(coll):
    """Delete given collection"""
    collection = database[coll]
    collection.delete_many({})

def DeleteById(coll, id):
    """Clear item in given collection with ObjectId"""
    collection = database[coll]
    collection.delete_one({'_id': ObjectId(id)})




# user = { "first_name": "Remco", "last_name": "Halman", "address": "Swannedrift 21", "zip_code": "9022 AR" }

# x = users.insert_one(user)