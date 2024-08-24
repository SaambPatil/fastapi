from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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
def create_post(post: Post):
    # print(new_post)
    print(post.dict())
    return {"data": f"{post.title}"}
