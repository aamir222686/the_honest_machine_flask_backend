from dotenv import load_dotenv
import os
import pymongo

# Loading .env file here
load_dotenv()

mongoConnString = os.getenv('MONGO_CONN_STR')
# Create post method

def getPostsByCount(count):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
    try:
        docs = []
        cursor = col.find({}).limit(int(count)).sort("date_added", -1)
        for document in cursor:
            docs.append(document)

        if len(docs):
            
            return docs
        else:
            
            return []

    except Exception as e:
        
        print("ERROR ::: ", e)
        return []
    finally:
        client.close()
    

def getPostsById(id):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
    try:
        docs = []
        cursor = col.find({"_id": str(id)})
        for document in cursor:
            docs.append(document)

        if len(docs):
            return docs
        else:
            return []

    except Exception as e:
        print("ERROR ::: ", e)
        return []
    finally:
        client.close()


def getPostsByCategory(category):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
    try:
        docs = []
        cursor = col.find({"category": str(category)}).sort("date_added", -1)
        for document in cursor:
            docs.append(document)

        if len(docs):
            return docs
        else:
            return []

    except Exception as e:
        print("ERROR ::: ", e)
        return []
    finally:
        client.close()
