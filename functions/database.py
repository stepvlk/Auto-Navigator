from pymongo import MongoClient
from config.config import config, base
import json
def dbase():
    dbase = f"mongodb://{config['db']['user']}:{config['db']['password']}@{config['db']['url']}"
    print(dbase)
    return dbase

connect = dbase()
client = MongoClient(connect)

def select_all(connections):
    try:
        collection = client[base][connections]
        result = []
        for res in collection.find({}, {"_id":0}):
            result.append(res)
        return {"data": result, "total_count": len(result)}
    except:
        return {"result": "no connect to database", "dbase": "Mongo", "data": []}

def select_raw(select, connections):
    try:
        collection = client[base][connections]
        data = []
        for res in collection.find(select, {"_id":0}):
            data.append(res)
        return {"data": data, "total_count": len(data)}
    except:
        return {"result": "no connect to database", "dbase": "Mongo", "data": []} 
    
def select_one(select, connections):
    try:
        collection = client[base][connections]
        data = collection.find_one(select, {"_id":0})
        return data
    except:
        return {"result": "no connect to database", "dbase": "Mongo", "data": {}}

def insert_data(data, connections):
    try:
        collection = client[base][connections]
        collection.insert_many(data['data'])
        return {"status": "insert"}
    except:
        return {"status": "fail"}

def insert_item(obj, connections):
    try:
        collection = client[base][connections]
        collection.insert_one(json.loads(obj))
        return {"status": "update"}
    except:
        return  {"status": "fail"}
