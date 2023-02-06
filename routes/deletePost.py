from dotenv import load_dotenv
import os
import pymongo

# Loading .env file here
load_dotenv()

mongoConnString = os.getenv('MONGO_CONN_STR')

# Create post method

def deletePost(req_info):
    client = pymongo.MongoClient(mongoConnString)
    db = client["posts"]
    col = db["posts"]
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
    finally:
        client.close()
