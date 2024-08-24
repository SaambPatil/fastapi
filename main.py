from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    

@app.get("/")
def root():
    return {"message": "Hello!!!! "}

@app.get("/posts")
def get_post():
    return {"message": "These are your posts!!!! "}


# @app.post("/createposts")
# def create_post(temp : dict = Body(...)):
#     print(temp)
#     return {"new_post": f"title {temp['title']} content: {temp['content']}"}

@app.post("/createposts")
def create_post(new_post : Post):
    print(new_post)
    # return {"new_post": f"title {temp['title']} content: {temp['content']}"}
    return {"data": f"{new_post.title}"}
