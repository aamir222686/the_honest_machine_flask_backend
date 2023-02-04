from dotenv import load_dotenv
import os
import pymongo

# Loading .env file here
load_dotenv()

mongoConnString = os.getenv('MONGO_CONN_STR')

client = pymongo.MongoClient(mongoConnString)
db = client["posts"]
col = db["posts"]


# Create post method

def deletePost(req_info):
    try:
        id = req_info["id"]
        res = col.delete_one({'_id': str(id)})
        if res.deleted_count > 0:
            return True
        else:
            return False

    except Exception as e:
        print("ERROR ::: ", e)
        return False
