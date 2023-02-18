from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os
fpath = os.path.join(os.path.dirname(__file__), 'routes')
sys.path.append(fpath)

# Custom module imports
from routes.createNewPost import createPost
from routes.updatePost import updatePost
from routes.deletePost import deletePost
from routes.getPosts import getPostsByCount, getPostsById
from routes.updateViewCount import updateViewCount

# Create ref to fastapi with app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', "https://thm-blog-website.vercel.app",
                   "https://thm-blog-website-aamir222686.vercel.app"],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
async def root():
    return "The App is alive....."


@app.post("/createNewPost")
async def root(data: Request):
    req_info = await data.json()
    res = createPost(req_info)
    if res == True:
        return {"status": 1}
    else:
        return {"status": 0}
    

@app.post("/updatePost")
async def root(data: Request):
    req_info = await data.json()
    res = updatePost(req_info)
    if res == True:
        return {"status": 1}
    else:
        return {"status": 0}
    

@app.post("/deletePost")
async def root(data: Request):
    req_info = await data.json()
    res = deletePost(req_info)
    if res == True:
        return {"status": 1}
    else:
        return {"status": 0}
    

@app.get("/getPostsById")
async def root(id):
    res = getPostsById(id)
    return res


@app.get("/getPostsByCount")
async def root(count):
    res = getPostsByCount(count)
    return res


@app.post("/updateViewCount")
async def root(data: Request):
    req_info = await data.json()
    res = updateViewCount(req_info)
    if res == True:
        return {"status": 1}
    else:
        return {"status": 0}
    

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')
