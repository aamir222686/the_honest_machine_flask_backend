from dotenv import load_dotenv
import os
import pymongo

# Loading .env file here
load_dotenv()

mongoConnString = os.getenv('MONGO_CONN_STR')
# Create post method

def updateViewCount(req_info):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
    try:
        id = req_info["id"]
        del req_info["id"]
        res = col.update_one({'_id': str(id)},  {"$inc": {"num_of_views": 1}})
        if res.modified_count > 0:
            
            return True
        else:
            
            return False

    except Exception as e:
        
        print("ERROR ::: ", e)
        return False
    finally:
        client.close()