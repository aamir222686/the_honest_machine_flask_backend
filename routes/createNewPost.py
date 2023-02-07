from dotenv import load_dotenv
import os
import pymongo
import datetime
import uuid

# Loading .env file here
load_dotenv()

mongoConnString = os.getenv('MONGO_CONN_STR')
# Create post method

def createPost(req_info):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
    try:
        req_info["_id"] = str(uuid.uuid4().split("-")[0])
        req_info["num_of_views"] = int(req_info["num_of_views"])
        req_info["date_added"] =  datetime.datetime.fromtimestamp(req_info["date_added"])
        res = col.insert_one(req_info)

        if len(res.inserted_id) > 0:
            
            return True
        else:
            
            return False
    except Exception as e:
        
        print("ERROR ::: ", e)
        return False
    finally:
        client.close()
